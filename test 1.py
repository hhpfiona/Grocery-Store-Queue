from store import GroceryStore, Customer, Item, NoAvailableLineError
from store import CheckoutLine, RegularLine, ExpressLine, SelfServeLine
import pytest

l1 = Customer('l1', [Item('butter', 10), Item('pate', 5),
                         Item('ham', 1), Item('milk', 1),
                         Item('strawberries', 15), Item('flour', 1),
                         Item('cream cheese', 2), Item('chocolate', 2),
                         Item('jam', 1)])
l2 = Customer('l2', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l3 = Customer('l3', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l4 = Customer('l4', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l5 = Customer('l5', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l6 = Customer('l6', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l7 = Customer('l7', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l8 = Customer('l8', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
l9 = Customer('l9', [Item('butter', 10), Item('pate', 5),
                     Item('ham', 1), Item('milk', 1),
                     Item('strawberries', 15), Item('flour', 1),
                     Item('cream cheese', 2), Item('chocolate', 2),
                     Item('jam', 1)])
s1 = Customer('s1', [Item('well-adjusted', 1), Item('grind', 5)])
s2 = Customer('s2', [Item('well-adjusted', 1), Item('grind', 5)])
s3 = Customer('s3', [Item('well-adjusted', 1), Item('grind', 5)])
s4 = Customer('s4', [Item('well-adjusted', 1), Item('grind', 5)])
s5 = Customer('s5', [Item('well-adjusted', 1), Item('grind', 5)])
s6 = Customer('s6', [Item('well-adjusted', 1), Item('grind', 5)])
s7 = Customer('s7', [Item('well-adjusted', 1), Item('grind', 5)])
s8 = Customer('s8', [Item('well-adjusted', 1), Item('grind', 5)])
s9 = Customer('s9', [Item('well-adjusted', 1), Item('grind', 5)])


class TestGroceryStore:
    """
    Tests for class GroceryStore.
    """
    def test_store_init(self):
        """
        Test class GroceryStore's initialization with example input files.
        """
        config_file_name = 'input_files/config_001_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 1

        config_file_name = 'input_files/config_010_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 1

        config_file_name = 'input_files/config_100_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 1

        config_file_name = 'input_files/config_100_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 1

        config_file_name = 'input_files/config_111_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 3

        config_file_name = 'input_files/config_111_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 3

        config_file_name = 'input_files/config_300_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 3

        config_file_name = 'input_files/config_300_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 3

        config_file_name = 'input_files/config_333_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 9

        config_file_name = 'input_files/config_333_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 9

        config_file_name = 'input_files/config_642_05.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.num_lines == 12

    def test_enter_line_fewest(self):
        """
        Test that customer joins line with the fewest other customers.
        """
        config_file_name = 'input_files/config_100_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()

        assert s.enter_line(s1) == 0
        assert s.enter_line(s2) == 0
        assert s.enter_line(s3) == 0

        config_file_name = 'input_files/config_111_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(s3) == 0
        assert s.enter_line(s4) == 1
        assert s.enter_line(s5) == 2

        config_file_name = 'input_files/config_100_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(s6) == 0
        with pytest.raises(NoAvailableLineError):
            s.enter_line(s7)
        with pytest.raises(NoAvailableLineError):
            s.enter_line(l1)

    def test_enter_line_express(self):
        """
        Test that when customer is ineligible for the express line, they
        do not join said line.
        """
        config_file_name = 'input_files/config_111_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(s1) == 0
        assert s.enter_line(l1) == 2

        config_file_name = 'input_files/config_111_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
        assert s.enter_line(s1) == 0
        assert s.enter_line(l1) == 2
        assert s.enter_line(l2) == 0
        assert s.enter_line(s2) == 1

    def test_enter_line_no_line(self):
        """
        Test that NoAvailableLineError is raised when there is no line.
        """
        config_file_name = 'input_files/config_100_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(l1) == 0
        with pytest.raises(NoAvailableLineError):
            s.enter_line(s1)

        config_file_name = 'input_files/config_010_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(s2) == 0
        with pytest.raises(NoAvailableLineError):
            s.enter_line(l2)

    def test_enter_line_tied_index(self):
        """
        Test that when the lines with the fewest customers are tied, customer
        joins the line with the lowest index.
        """
        config_file_name = 'input_files/config_300_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(l1) == 0
        assert s.enter_line(s1) == 1
        assert s.enter_line(l2) == 2

        config_file_name = 'input_files/config_222_02.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert s.enter_line(l1) == 0
        assert s.enter_line(s1) == 1
        assert s.enter_line(l2) == 4
        assert s.enter_line(s2) == 2
        assert s.enter_line(l3) == 5
        assert s.enter_line(s3) == 3
        assert s.enter_line(l4) == 0
        assert s.enter_line(s4) == 1
        assert s.enter_line(l5) == 4
        assert s.enter_line(s5) == 2

    def test_next_checkout_time(self):
        """
        Test next_checkout_time's functionality for RegularLine, ExpressLine,
        and SelfServeLine.
        """
        config_file_name = 'input_files/config_111_01.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        c1 = Customer('Fiona', [Item('bananas', 7), Item('apples', 5)])
        c2 = Customer('Han', [Item('broth', 2)])
        c3 = Customer('Ryan', [Item('yogurt', 4), Item('salami', 4),
                               Item('ham', 1), Item('milk', 1),
                               Item('strawberries', 15), Item('flour', 1),
                               Item('cream cheese', 2), Item('chocolate', 2),
                               Item('jam', 1)])
        assert type(s.lines[0]) is RegularLine
        assert type(s.lines[1]) is ExpressLine
        assert type(s.lines[2]) is SelfServeLine

        assert s.enter_line(c1) == 0
        assert s.enter_line(c2) == 1
        assert s.enter_line(c3) == 2
        assert s.next_checkout_time(0) == 12
        assert s.next_checkout_time(1) == 2
        assert s.next_checkout_time(2) == 62

    def test_remove_front_customer(self):
        """
        Test remove_front_customer's functionality for RegularLine, ExpressLine,
        and SelfServeLine.
        """
        config_file_name = 'input_files/config_111_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()
        assert type(s.lines[0]) is RegularLine
        assert type(s.lines[1]) is ExpressLine
        assert type(s.lines[2]) is SelfServeLine

        assert s.enter_line(s1) == 0
        assert s.enter_line(s2) == 1
        assert s.enter_line(l1) == 2
        assert s.enter_line(s3) == 0
        assert s.remove_front_customer(0) == 1
        assert s.remove_front_customer(0) == 0
        assert s.remove_front_customer(1) == 0
        assert s.remove_front_customer(2) == 0
        assert s.remove_front_customer(2) == 0

    def test_close(self):
        """
        Check close_line's functionality for RegularLine, ExpressLine,
        and SelfServeLine.
        """
        config_file_name = 'input_files/config_111_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()

        assert type(s.lines[0]) is RegularLine
        assert type(s.lines[1]) is ExpressLine
        assert type(s.lines[2]) is SelfServeLine

        assert s.enter_line(s1) == 0
        assert s.enter_line(s2) == 1
        assert s.enter_line(l1) == 2
        assert s.enter_line(s3) == 0
        assert s.enter_line(l2) == 2
        assert s.enter_line(l3) == 0
        assert s.enter_line(l4) == 2
        assert s.enter_line(l5) == 0

        assert s.lines[0].is_open is True
        assert s.lines[1].is_open is True
        assert s.lines[2].is_open is True

        assert s.close_line(0) == [s3, l3, l5]
        assert s.close_line(1) == []
        assert s.close_line(2) == [l2, l4]

        assert s.lines[0].is_open is False
        assert s.lines[1].is_open is False
        assert s.lines[2].is_open is False

    def test_first_in_line(self):
        """
        Check first_in_line's functionality for RegularLine, ExpressLine,
        and SelfServeLine.
        """
        config_file_name = 'input_files/config_100_10.json'
        with open(config_file_name) as config_file:
            s = GroceryStore(config_file)
            config_file.close()

        assert s.first_in_line(0) is None
        assert s.enter_line(s1) == 0
        assert s.enter_line(s2) == 0
        assert s.enter_line(s3) == 0
        assert s.enter_line(s4) == 0
        assert s.enter_line(s5) == 0
        assert s.first_in_line(0) is s1
        assert s.remove_front_customer(0) == 4
        assert s.first_in_line(0) is s2
        assert s.remove_front_customer(0) == 3
        assert s.first_in_line(0) is s3
        assert s.remove_front_customer(0) == 2
        assert s.first_in_line(0) is s4
        assert s.remove_front_customer(0) == 1
        assert s.first_in_line(0) is s5
        assert s.remove_front_customer(0) == 0
        assert s.first_in_line(0) is None


item_list = [Item('bananas', 7), Item('applies', 3),
             Item('strawberries', 13), Item('mango', 5)]
fio = Customer('Fiona', item_list)
rymie = Customer('Ryan', [])


class TestCustomer:
    """
    Tests for class Customer.
    """
    def test_customer_init(self):
        """
        Test class Customer's initialization.
        """
        assert fio.name == 'Fiona'
        assert fio._items == item_list
        assert fio._items is not item_list
        assert fio.arrival_time is None

        assert rymie.name == 'Ryan'
        assert rymie._items == []
        assert rymie.arrival_time is None

    def test_customer_num_items(self):
        """
        Test that num_items returns 0 when customer has no items or the correct
        number of items otherwise.
        """
        assert fio.num_items() == 4
        assert rymie.num_items() == 0

    def test_customer_item_time(self):
        """
        Test that item_time returns 0 when the customer has no items or the
        correct time otherwise.
        """
        assert fio.item_time() == 28
        assert rymie.item_time() == 0


class TestItem:
    """
    Tests for class Item.
    """
    def test_item_init(self):
        """
        Test class Item's initialization.
        """
        item1 = Item('self-esteem', 2)
        item2 = Item('chicken', 3)
        assert item1.name == 'self-esteem'
        assert item1.time == 2
        assert item2.name == 'chicken'
        assert item2.time == 3


class TestCheckoutLine:
    """
    Tests for subclasses RegularLine, ExpressLine, and SelfServeLine of parent
    class CheckoutLine.
    """
    def test_line_init(self):
        """
        Test initializers of RegularLine, ExpressLine, and SelfServeLine.
        """
        c = CheckoutLine(4)
        r = RegularLine(3)
        e = ExpressLine(2)
        s = SelfServeLine(1)
        assert c.is_open is True
        assert r.is_open is True
        assert e.is_open is True
        assert s.is_open is True
        assert c.capacity == 4
        assert r.capacity == 3
        assert e.capacity == 2
        assert s.capacity == 1

    def test_line_len(self):
        """
        Test method len of CheckoutLine.
        """
        c = CheckoutLine(4)
        assert c.__len__() == 0
        c.accept(fio)
        assert c.__len__() == 1
        c.accept(rymie)
        assert c.__len__() == 2

    def test_line_can_accept(self):
        """
        Test method can_accept of CheckoutLine.
        """
        e = ExpressLine(2)
        s = SelfServeLine(1)

        assert s.is_open is True
        s.accept(fio)
        assert s.can_accept(rymie) is False
        s.close()
        assert s.is_open is False
        assert s.can_accept(fio) is False

        assert e.is_open is True
        assert e.can_accept(s1) is True
        e.accept(s1)
        assert e.can_accept(s2) is True

    def test_line_accept(self):
        """
        Test method accept of CheckoutLine and subclasses RegularLine,
        ExpressLine, and SelfServeLine.
        """
        c = CheckoutLine(4)
        s = SelfServeLine(1)

        assert len(c) == 0
        assert c.can_accept(s1) is True
        assert c.accept(s1) is True
        assert c.first_in_line() is s1
        assert len(c) == 1

        assert len(s) == 0
        assert s.can_accept(s2) is True
        assert s.accept(s2) is True
        assert s.first_in_line() is s2
        assert len(s) == 1
        assert s.can_accept(s3) is False
        assert s.accept(s3) is False
        assert s.first_in_line() is s2
        assert len(s) == 1

    def test_next_checkout_time(self):
        """
        Test method next_checkout_time for CheckoutLine and subclasses
        RegularLine, ExpressLine, and SelfServeLine.
        """
        r = RegularLine(3)
        e = ExpressLine(2)
        s = SelfServeLine(1)

        r.accept(fio)
        r.accept(rymie)
        r.accept(s1)
        assert r.next_checkout_time() == 28
        r.remove_front_customer()
        assert r.next_checkout_time() == 0
        r.remove_front_customer()
        assert r.next_checkout_time() == 6

        e.accept(fio)
        e.accept(rymie)
        assert e.next_checkout_time() == 28
        e.remove_front_customer()
        assert e.next_checkout_time() == 0

        s.accept(s1)
        assert s.next_checkout_time() == 12

    def test_remove_front_customer(self):
        """
        Test method remove_front_customer for CheckoutLine and subclasses
        RegularLine, ExpressLine, and SelfServeLine.
        """
        r = RegularLine(3)
        e = ExpressLine(2)
        s = SelfServeLine(1)

        r.accept(s1)
        r.accept(s2)
        r.accept(s3)
        assert r.first_in_line() is s1
        assert r.remove_front_customer() == 2
        assert r.first_in_line() is s2
        assert r.remove_front_customer() == 1
        assert r.first_in_line() is s3
        assert r.remove_front_customer() == 0
        assert r.first_in_line() is None

        e.accept(s1)
        e.accept(s2)
        assert e.first_in_line() is s1
        assert e.remove_front_customer() == 1
        assert e.first_in_line() is s2
        assert e.remove_front_customer() == 0

        s.accept(s1)
        assert s.first_in_line() is s1
        assert s.remove_front_customer() == 0

    def test_close(self):
        """
        Check method close_line for RegularLine, ExpressLine,
        and SelfServeLine.
        """
        r = RegularLine(3)
        e = ExpressLine(2)
        s = SelfServeLine(1)

        r.accept(s1)
        r.accept(s2)
        r.accept(s3)
        assert r.close() == [s2, s3]
        assert r.is_open is False

        e.accept(s1)
        e.accept(s2)
        assert e.close() == [s2]
        assert e.is_open is False

        s.accept(s1)
        assert s.close() == []
        assert s.is_open is False

    def test_first_in_line(self):
        """
        Check method first_in_line for RegularLine, ExpressLine,
        and SelfServeLine.

        check that when no one is in line, return None
        when 1 customer in line, they are returned
        when 1+, check that front customer is returned
        """
        r = RegularLine(3)
        e = ExpressLine(2)
        s = SelfServeLine(1)

        r.accept(s1)
        r.accept(s2)
        r.accept(s3)
        assert r.first_in_line() is s1

        e.accept(s4)
        assert e.first_in_line() is s4

        assert s.first_in_line() is None


if __name__ == '__main__':
    pytest.main(['test 1.py'])
