from project import Scheduler, Task

def test_add_task():
    scheduler = Scheduler()

    scheduler.add_task("Task 1", 1)

    assert len(scheduler.tasks) == 1
    assert scheduler.tasks[0].name == "Task 1"
    assert scheduler.tasks[0].duration == 1


def test_run(capsys):
    scheduler = Scheduler()

    scheduler.add_task("Task 1", 1)

    scheduler.run()

    captured = capsys.readouterr()

    assert "🕒 Starting task: Task 1" in captured.out
    assert "✅ Completed task: Task 1" in captured.out


def test_notify_me(capsys):

    scheduler = Scheduler()

    scheduler.notify_me("Test notification")

    captured = capsys.readouterr()

    assert "Test notification" in captured.out

# Test for adding a task with a duration of 1 minute.
