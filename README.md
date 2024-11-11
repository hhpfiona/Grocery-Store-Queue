# Grocery Store Simulation [February - March 2024]

This repository contains a project to build an **Event-Driven Grocery Store Simulation**. This tool models customer arrivals, checkout processes, and line management strategies to help grocery stores optimize checkout staffing based on customer flow throughout the day.

## Project Overview

Grocery stores face a constant challenge in managing checkout lines efficiently. An excess of open lines increases staffing costs, while too few lines can lead to long customer wait times. This simulation is designed to model various types of checkout lines—regular, express, and self-serve—and simulate events such as customer arrivals and line closures to help stores optimize operations and improve customer satisfaction.

### Key Components

1. **Customers**: Each customer has a unique name and a specific number of items.
2. **Checkout Lines**: There are three types:
   - **Regular**: Open to all customers.
   - **Express**: Only for customers with fewer than 8 items.
   - **Self-Serve**: Open to all customers, but checkout takes longer as customers serve themselves.
3. **Events**: The simulation operates on a series of timestamped events, including:
   - **Customer Arrival**
   - **Checkout Started**
   - **Checkout Completed**
   - **Close Line**

## Features and Structure

- **`store.py`**: Manages store and checkout lines, modeling customer interactions at each type of checkout line.
- **`event.py`**: Defines event types and processes incoming events through an event list.
- **`simulation.py`**: Drives the overall simulation, managing the event queue and generating key statistics.
- **`container.py`**: Implements a `PriorityQueue` for sorting events by timestamp.
- **Configuration Files**:
  - **`input_files/config_*.json`**: Configures store setup with parameters for different checkout line types and capacities.
  - **`input_files/events_*.txt`**: Contains customer arrival and line closure events for the simulation.

## Project Tasks

### Task 1: Modeling the Grocery Store

In `store.py`, implement models for the store, customers, and different checkout lines. Define each class’s attributes and methods to capture the real-world operation of a grocery store checkout system.

### Task 2: Defining Event Types

In `event.py`, create subclasses for each event type (e.g., Customer Arrival, Checkout Started, Checkout Completed, Close Line) and implement the `create_event_list` function to read events from an input file and populate the event queue.

### Task 3: Implementing Priority Queue

Develop a `PriorityQueue` in `container.py` to manage events efficiently by timestamp. This will ensure events are processed in the correct order to maintain the simulation flow.

### Task 4: Running the Simulation

The `GroceryStoreSimulation.run` method in `simulation.py` drives the main simulation loop, processing events in sequence and updating the simulation’s statistics. The loop:
1. Processes each event in sequence.
2. Updates the simulation’s state and gathers statistics, including total customer count, total simulation time, and maximum wait time.

## Key Statistics

Once the simulation completes, it reports:
- **Total Customers**: The number of customers processed.
- **Total Simulation Time**: Timestamp of the final event.
- **Maximum Wait Time**: Longest wait time experienced by any customer.

## Setup and Execution

1. Clone this repository.
2. Place any configuration and event files in the designated folders.
3. Run `simulation.py` to start the simulation.
4. Use `pytest` for unit tests provided in `test_priority_queue.py`.

## Testing

- `test 0.py` validates the entire simulation.
- `test 1.py` validates store.py.
- `test 2.py` validates event.py
- `check_coverage.py` assesses code coverage.
- `python_ta.check_all()` is available to ensure Python code style compliance.

## Future Directions

This simulation could be expanded with additional customer behavior models, such as customer impatience or line-switching. Analyzing the results across different configurations could provide further insights into effective staffing and line management strategies in grocery stores.

