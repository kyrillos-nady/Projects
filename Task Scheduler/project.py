import sys
import time
import threading


class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.elapsed_time = 0


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, duration):
        task = Task(name, duration)
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            print(f"🕒 Starting task: {task.name}. Duration: {task.duration} minutes.")
            self.notify_me(f"It's time to work on {task.name}.")
            start_time = time.time()
            while task.elapsed_time < task.duration * 60:
                task.elapsed_time = time.time() - start_time
                remaining_time = (task.duration * 60) - task.elapsed_time
                print(f"⏱ Task: {task.name}. Remaining time: {remaining_time:.0f} seconds", end="\r")
                time.sleep(1)
            print(f"\n✅ Completed task: {task.name}")

    def notify_me(self, msg):
        print(msg)
        # Here you can implement notification logic for your specific platform


def main():
    try:
        scheduler = Scheduler()

        while True:
            print("\n📝 Task Scheduler")
            print("1. Add Task")
            print("2. Start Scheduler")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter task name: ")
                duration = int(input("Enter task duration (minutes): "))
                scheduler.add_task(name, duration)
                print("Task added successfully!")

            elif choice == "2":
                if not scheduler.tasks:
                    print("No tasks added yet.")
                else:
                    scheduler_thread = threading.Thread(target=scheduler.run)
                    scheduler_thread.start()
                    scheduler_thread.join()

            elif choice == "3":
                print("Exiting...\n👋 Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
