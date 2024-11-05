from __future__ import annotations
from typing import TextIO
import json

# The maximum number of items a customer can have if they use an express line.
EXPRESS_LIMIT = 7


class NoAvailableLineError(Exception):
    """Represents a situation in which a customer has arrived at the checkout
    area and there is no line available for them to join.
    """

    def __str__(self) -> str:
        return 'No line available'


class GroceryStore:
    """A grocery store.

    A grocery store consists of checkout lines.

    Attributes:
    - num_lines:
        How many lines this grocery store has.
    - lines:
        a list of the lines in this grocery store. Lines are referred to by a
        unique index, with the following order: regular lines, express lines,
        and then self-serve lines.

    Representation Invariants:
    - self.num_lines > 0
    - len(self.lines) > 0
    """
    num_lines: int
    lines: list[CheckoutLine]

    def __init__(self, config_file: TextIO) -> None:
        """Initialize a GroceryStore from a configuration file <config_file>.

        Preconditions:
        - config_file is a valid JSON configuration file with the keys
          regular_count, express_count, self_serve_count, and line_capacity
        - config_file is open
        - All values in config_file are >= 0
        """
        self.lines = []
        file = json.load(config_file)
        self.num_lines = (file['regular_count'] + file['express_count']
                          + file['self_serve_count'])

        for _ in range(file['regular_count']):
            self.lines.append(RegularLine(file['line_capacity']))
        for _ in range(file['express_count']):
            self.lines.append(ExpressLine(file['line_capacity']))
        for _ in range(file['self_serve_count']):
            self.lines.append(SelfServeLine(file['line_capacity']))

    def enter_line(self, customer: Customer) -> int:
        """Pick a new line for <customer> to join, using the algorithm from
        the handout and add <customer> to that line.

        Return the index of the line that the customer joined.

        Raise a NoAvailableLineError if there is no line available for the
        customer to join.

        Preconditions:
        - customer is not currently in any line in this GroceryStore
        """
        i = 0
        line = self.lines[i]
        while not line.can_accept(customer) and i + 1 < self.num_lines:
            i += 1
            line = self.lines[i]
        available_line = line
        available_index = i
        for line in self.lines:
            if line.can_accept(customer):
                if (len(line) < len(available_line)
                        or (len(line) == len(available_line)
                            and i < available_index)):
                    available_line = line
                    available_index = i
            i += 1
        if available_line.accept(customer):
            return available_index
        else:
            raise NoAvailableLineError

    def next_checkout_time(self, line_number: int) -> int:
        """Return the time it will take to check out the customer at the front
        of line <line_number>.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        return self.lines[line_number].next_checkout_time()

    def remove_front_customer(self, line_number: int) -> int:
        """If there is any customer (or customers) in checkout line
        <line_number>, remove the front customer.

        Return the number of customers remaining in line <line_number>.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        return self.lines[line_number].remove_front_customer()

    def close_line(self, line_number: int) -> list[Customer]:
        """Close checkout line <line_number> by updating its status to indicate
        that it is closed and removing from it all customers after the first
        one.

        Return a new list with these removed customers, in the same order as
        they appeared in the line before it closed.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        return self.lines[line_number].close()

    def first_in_line(self, line_number: int) -> Customer | None:
        """Return the first customer in line <line_number>, or None if there
        are no customers in line.

        Do not change the line, however.

        Preconditions:
        - 0 <= line_number < self.num_lines
        """
        return self.lines[line_number].first_in_line()


class Customer:
    """A grocery store customer.

    Attributes:
    - name: A unique identifier for this customer.
    - arrival_time: The first time this customer arrived at the checkout area
      and attempted to join a line, or None if they have not yet arrived.
    - _items: The items this customer has.

    Representation Invariants:
    - self.arrival_time is None or self.arrival_time >= 0
    """
    name: str
    arrival_time: int | None
    _items: list[Item]

    def __init__(self, name: str, items: list[Item]) -> None:
        """Initialize a customer with the given <name> and a copy of the
        list <items>.

        The customer's arrival_time is initially None.

        >>> item_list = [Item('bananas', 7)]
        >>> belinda = Customer('Belinda', item_list)
        >>> belinda.name
        'Belinda'
        >>> belinda._items == item_list
        True
        >>> belinda._items is item_list
        False
        >>> belinda.arrival_time is None
        True
        """
        items_copy = items.copy()
        self.name = name
        self._items = items_copy
        self.arrival_time = None

    def num_items(self) -> int:
        """Return the number of items this customer has.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.num_items()
        2
        """
        return len(self._items)

    def item_time(self) -> int:
        """Return the number of seconds it takes for a cashier to check out
        this customer, that is, the time it takes to check out this customer
        at a regular or express line.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.item_time()
        10
        """
        time = 0
        for item in self._items:
            time += item.time
        return time

    def __str__(self) -> str:
        """
        Return a string representation of this customer in the form of name.
        """
        return self.name


class Item:
    """An item to be checked out.

    Attributes:
    - name: the name of this item
    - time: the amount of time it takes a cashier to check out this item

    Representation Invariants:
    - self.time > 0
    """
    name: str
    time: int

    def __init__(self, name: str, time: int) -> None:
        """Initialize a new item with <name> and <time>.

        Preconditions:
        - time > 0

        >>> item = Item('bananas', 7)
        >>> item.name
        'bananas'
        >>> item.time
        7
        """
        self.name = name
        self.time = time


class CheckoutLine:
    """A checkout line in a grocery store.

    This is an abstract class and should not be instantiated.

    Attributes:
    - capacity: The maximum number of customers allowed in this CheckoutLine.
    - is_open: True iff the line is open.
    - _queue: Customers in this line are in order by arrival time, with the
                earliest arrival at the front of the list.

    Representation Invariants:
    - len(self) <= self.capacity
    - self.capacity > 0
    """
    capacity: int
    is_open: bool
    _queue: list[Customer]

    def __init__(self, capacity: int) -> None:
        """Initialize an open and empty CheckoutLine, with the given <capacity>.

        Preconditions:
        - capacity > 0

        >>> line = CheckoutLine(1)
        >>> line.capacity
        1
        >>> line.is_open
        True
        >>> line._queue
        []
        """
        self._queue = []
        self.capacity = capacity
        self.is_open = True

    def __len__(self) -> int:
        """Return the length of this CheckoutLine.

        >>> line = CheckoutLine(10)
        >>> len(line)
        0
        """
        return len(self._queue)

    def can_accept(self, customer: Customer) -> bool:
        """Return True iff this CheckoutLine can accept <customer>.

        >>> line = CheckoutLine(1)
        >>> line.can_accept(Customer('Sophia', []))
        True
        """
        if self.is_open and len(self) < self.capacity:
            if isinstance(customer, Customer):
                return True
        return False

    def accept(self, customer: Customer) -> bool:
        """Accept <customer> into the end of this CheckoutLine if possible.

        Return True iff the customer is accepted.

        >>> line = CheckoutLine(1)
        >>> c1 = Customer('Belinda', [Item('cheese', 3)])
        >>> c2 = Customer('Hamman', [Item('chips', 4), Item('gum', 1)])
        >>> line.accept(c1)
        True
        >>> line.accept(c2)
        False
        >>> len(line)
        1
        >>> line.first_in_line() is c1
        True
        """
        if self.can_accept(customer):
            self._queue.append(customer)
            return True
        return False

    def next_checkout_time(self) -> int:
        """Return the time it will take to check out the customer at the front
        of this line.

        Preconditions:
        - self.first_in_line() is not None

        No doctests provided, since this method is abstract.
        """
        raise NotImplementedError

    def remove_front_customer(self) -> int:
        """If there is any customer (or customers) in this checkout line,
        remove the front customer.

        Return the number of customers remaining in the line.

        >>> line = CheckoutLine(1)
        >>> line.accept(Customer('Sophia', [Item('red snapper', 21)]))
        True
        >>> line.remove_front_customer() # No one is left in line.
        0
        >>> line.remove_front_customer() # It's still okay to call the method.
        0
        """
        if len(self) != 0:
            self._queue.pop(0)
        return len(self)

    def close(self) -> list[Customer]:
        """Close this line by updating its status to indicate that it is closed
        and removing from it all customers after the first one.

        Return a new list with these removed customers, in the same order as
        they appeared in the line before it closed.

        >>> line = CheckoutLine(2)
        >>> line.close()
        []
        >>> line.is_open
        False
        """
        self.is_open = False
        customers = []
        if len(self) != 0:
            while len(self) != 1:
                customers.insert(0, self._queue.pop())
        return customers

    def first_in_line(self) -> Customer | None:
        """Return the first customer in this line, or None if there are no
        customers in line.

        Do not change the line, however.

        >>> line = CheckoutLine(1)
        >>> line.first_in_line() is None
        True
        """
        if len(self) != 0:
            return self._queue[0]
        return None


class RegularLine(CheckoutLine):
    """A regular CheckoutLine.

    A subclass of class CheckoutLine, and is found in Grocery store.

    Representation Invariants
    - len(self) <= self.capacity
    - self.capacity > 0
    """

    def __init__(self, capacity: int) -> None:
        CheckoutLine.__init__(self, capacity)

    def next_checkout_time(self) -> int:
        """Return the time it will take to check out the customer at the front
        of this line.

        The time required to check out is equal to the total time required for
            each of the customer's items to be checked out by a cashier.

        Preconditions:
        - self.first_in_line() is not None

        >>> line = RegularLine(3)
        >>> c1 = Customer('Belinda', [Item('cheese', 3)])
        >>> c2 = Customer('Hamman', [Item('chips', 4), Item('gum', 1)])
        >>> line.accept(c1)
        True
        >>> line.accept(c2)
        True
        >>> line.next_checkout_time()
        3
        """
        return self._queue[0].item_time()


class ExpressLine(CheckoutLine):
    """An express CheckoutLine.

    A customer is only allowed to enter an express CheckoutLine if they have
    fewer than 8 items
    """
    def __init__(self, capacity: int) -> None:
        CheckoutLine.__init__(self, capacity)

    def next_checkout_time(self) -> int:
        """Return the time it will take to check out the customer at the front
        of this line in seconds.

        The time required to check out is equal to the total time required for
           each of the customer's items to be checked out by a cashier.

        Preconditions:
        - self.first_in_line() is not None
        """
        return self._queue[0].item_time()

    def can_accept(self, customer: Customer) -> bool:
        """Return True whether this express line can accept <customer>, False
        otherwise. A customer can only enter an express line if it has space,
        and if the customer has fewer than 8 items.

        >>> line = ExpressLine(3)
        >>> c1 = Customer('Belinda', [Item('cheese', 3)])
        >>> c2 = Customer('Hamman', [Item('chips', 4),
        ...                          Item('gum', 1),
        ...                          Item('chips', 10),
        ...                          Item('chips', 4),
        ...                          Item('gum', 1),
        ...                          Item('chips', 10),
        ...                          Item('ToiletPaper', 20),
        ...                          Item('milk', 4)])
        >>> line.accept(c1)
        True
        >>> line.accept(c2)
        False
        """
        if len(self) < self.capacity and customer.num_items() < 8:
            return True
        return False


class SelfServeLine(CheckoutLine):
    """A self-serve CheckoutLine.
    """

    def __init__(self, capacity: int) -> None:
        CheckoutLine.__init__(self, capacity)

    def next_checkout_time(self) -> int:
        """Return the next checkout time of the first customer in line
        in seconds.

        The time it takes a customer to check out is double the time that it
        takes for a cashier to check that customer out.

        >>> line = SelfServeLine(3)
        >>> c2 = Customer('Hamman', [Item('chips', 4), Item('gum', 1)])
        >>> line.accept(c2)
        True
        >>> line.next_checkout_time()
        10
        """
        return self._queue[0].item_time() * 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
