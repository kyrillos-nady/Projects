# Task Scheduler

#### Description: Task Scheduler Application

The Task Scheduler Application is a Python-based tool designed to help users manage their tasks efficiently. This application allows users to add tasks with specific durations, run the scheduler to execute these tasks, and receive notifications when tasks start and complete. It offers a simple command-line interface for ease of use.

### Features

- **Task Management**: Users can add tasks with names and durations to the scheduler.
- **Time Tracking**: The application tracks the elapsed time for each task and displays the remaining time.
- **Notifications**: Users receive notifications when tasks start and complete.
- **User Interaction**: The command-line interface allows users to interact with the scheduler easily.

### Usage

1. **Add Task**: To add a task, follow these steps:
   - Launch the application.
   - Choose option `1` from the menu.
   - Enter the task name and duration when prompted.

2. **Start Scheduler**: To start the scheduler and execute tasks, follow these steps:
   - Choose option `2` from the menu.
   - The scheduler will run all added tasks sequentially.

3. **Exit**: To exit the application, choose option `3` from the menu.

### Implementation Details

- **Task Class**: Defines a task with attributes such as name, duration, and elapsed time.
- **Scheduler Class**: Manages tasks and their execution. Includes methods to add tasks and run the scheduler.
- **Notification System**: Displays notifications for task events using print statements.

### How to Run Tests

To ensure the application functions correctly, tests have been implemented using the `pytest` framework. These tests verify the functionality of adding tasks, running the scheduler, and receiving notifications.

```python
# Running Tests
$ pytest test_code.py
```

Test Description
test_add_task: Verifies that a task with a duration of 1 minute is added correctly.
test_run: Checks if the scheduler correctly starts and completes a task with the expected output.
test_notify_me: Ensures that the notification system displays the correct message.
Note: This application provides a basic task scheduling functionality. Additional features such as persistent storage, more robust notification systems, and improved user interfaces can be implemented for enhanced usability and functionality.
