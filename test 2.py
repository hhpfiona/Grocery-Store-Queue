from __future__ import annotations
from typing import TextIO
from io import StringIO
from simulation import GroceryStoreSimulation
from event import Event, create_event_list, CustomerArrival, CheckoutCompleted
from store import GroceryStore, Customer, Item, NoAvailableLineError
from store import CheckoutLine, RegularLine, ExpressLine, SelfServeLine
from container import PriorityQueue
import pytest


def test_simulation_run_demo() -> None:
    """
    Test running grocery simulations on events_base.
    """
    config_file_name = 'input_files/config_111_03.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_demo.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    assert sim.stats == {'num_customers': 6, 'total_time': 120, 'max_wait': 115}


def test_simulation_run_events_base() -> None:
    """
    Test running grocery simulations on events_base.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    assert sim.stats == {'num_customers': 6, 'total_time': 87, 'max_wait': 22}

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    assert sim.stats == {'num_customers': 6, 'total_time': 76, 'max_wait': 11}

    config_file_name = 'input_files/config_643_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    assert sim.stats == {'num_customers': 6, 'total_time': 76, 'max_wait': 11}


def test_simulation_run_events_mixtures() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


def test_simulation_run_events_no_express() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


def test_simulation_run_events_one() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


def test_simulation_run_events_one_at_a_time() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


def test_simulation_run_events_one_close() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


def test_simulation_run_events_two() -> None:
    """
    Test running grocery simulations on events_mixtures.
    """
    config_file_name = 'input_files/config_111_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_333_10.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)

    config_file_name = 'input_files/config_642_05.json'
    with open(config_file_name) as config_file:
        sim = GroceryStoreSimulation(config_file)
        config_file.close()
    event_file_name = 'input_files/events_base.txt'
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    sim.run(events)
    print(sim.stats)


if __name__ == '__main__':
    pytest.main(['test 2.py'])
