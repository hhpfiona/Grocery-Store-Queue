from container import PriorityQueue


def test_priority_remove_1() -> None:
    """Test method remove by clearing an entire queue."""
    pq = PriorityQueue()
    pq.add(4)
    pq.add(3)
    pq.add(2)
    pq.add(1)
    while not pq.is_empty():
        pq.remove()
    assert pq.is_empty()


def test_priority_queue_add_empty_list() -> None:
    """Test method add by adding one item to an empty list."""
    pq = PriorityQueue()
    pq.add(1)
    assert pq.remove() == 1


def test_priority_queue_highest_priority() -> None:
    """Test method add to create a queue of length 5 and check that the item
    at index 0 has the highest priority.
    """
    pq = PriorityQueue()
    pq.add(5)
    pq.add(4)
    pq.add(8)
    pq.add(1)
    assert pq.remove() == 1


def test_priority_queue_add_last_item() -> None:
    """Test method add and check that the last item added is at the end of
    the queue.
    """
    pq = PriorityQueue()
    pq.add(10)
    pq.add(15)
    pq.add(11)
    pq.add(20)
    pq.remove()
    pq.remove()
    pq.remove()
    assert pq.remove() == 20


def test_priority_queue_add_duplicates() -> None:
    """Test method add in the PriorityQueue class with duplicates of the
    same number, with one item that has a lower priority than the rest."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(1)
    pq.add(1)
    pq.add(1)
    pq.add(2)
    assert pq.remove() == 1
    assert pq.remove() == 1
    assert pq.remove() == 1
    assert pq.remove() == 1
    assert pq.remove() == 2
    assert pq.is_empty()


def test_priority_queue_check_order_1() -> None:
    """Test method add in the PriorityQueue class by checking that each item
    added to the queue is in the proper order"""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(1)
    pq.add(50)
    pq.add(51)
    pq.add(1)
    pq.add(5)
    pq.add(62)
    assert pq.remove() == 1
    assert pq.remove() == 1
    assert pq.remove() == 1
    assert pq.remove() == 5
    assert pq.remove() == 50
    assert pq.remove() == 51
    assert pq.remove() == 62
    assert pq.is_empty()


def test_priority_queue_check_order_2() -> None:
    """Test method add from the PriorityQueue class by checking that items
    added are in the proper order."""
    pq = PriorityQueue()
    pq.add(2)
    pq.add(2)
    pq.add(5)
    pq.add(5)
    pq.add(3)
    pq.add(1)
    pq.add(27)
    pq.add(26)
    assert pq.remove() == 1
    assert pq.remove() == 2
    assert pq.remove() == 2
    assert pq.remove() == 3
    assert pq.remove() == 5
    assert pq.remove() == 5
    assert pq.remove() == 26
    assert pq.remove() == 27
    assert pq.is_empty()


def test_priority_queue_q_is_empty() -> None:
    """Test method is_empty"""
    pq = PriorityQueue()
    pq.add(6)
    pq.add(5)
    pq.add(6)
    pq.add(5)
    pq.add(6)
    pq.add(5)
    assert pq.remove() == 5
    assert pq.remove() == 5
    assert pq.remove() == 5
    assert pq.remove() == 6
    assert pq.remove() == 6
    assert pq.remove() == 6
    assert pq.is_empty()


def test_priority_queue_add_str_1() -> None:
    """Test method is_empty"""
    pq = PriorityQueue()
    pq.add('more')
    pq.add('cake')
    pq.add('please')
    assert pq.remove() == 'cake'
    assert pq.remove() == 'more'
    assert pq.remove() == 'please'


def test_priority_queue_fifo_order() -> None:
    """Test priority to ensure that FIFO order is respected."""
    pq = PriorityQueue()
    pq.add(5)
    pq.add(5)
    pq.remove()
    assert pq.remove() == 5


def test_priority_queue_not_empty() -> None:
    """Test priority to ensure that FIFO order is respected."""
    pq = PriorityQueue()
    pq.add(5)
    pq.add(5)
    pq.remove()
    assert not pq.is_empty()


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
