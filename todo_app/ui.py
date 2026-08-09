import subprocess
import sys

def clear_screen() -> None:
    if sys.platform == "win32":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def wait_for_user() -> None:
    while True:
        user_input = input("\nPress Enter to continue...")

        if user_input == "":
            return

        print("\nInvalid input. Please press Enter only.")

def print_menu(title: str, options: list[str] | None = None, width: int = 50) -> None:
    border = "=" * width
    
    print(f"\n╔{border}╗")
    print(f"║{title:^{width}}║") # The symbol ^ means center the text.

    if options:
        print(f"╠{border}╣")

        for number, option in enumerate(options, start=1):
            prefix = f" {number}. "
            print(f"║{prefix}{option:<{width - len(prefix)}}║") # The symbol < means left-align the text.

    print(f"╚{border}╝")

def add_task_ui(manager):
    print_menu("Adding Task")

    title = input("\nTitle: ")

    if not title:
        print("\nTitle shouldn't be empty!\n")
        return

    description = input("\nDescription: ")

    print_menu("Set Priority", ["High", "Medium", "Low"])

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        choice = 3

    priority = {
        1: "High",
        2: "Medium",
        3: "Low",
    }.get(choice, "Low")

    manager.add_task(title, description, priority)

    print("\nNew task added successfully.\n")

def remove_task_ui(manager):
    print_menu("Removing a Task")

    uuid = input("\nEnter UUID: ")

    if manager.remove_task(uuid):
        print("\nTask removed.\n")
    else:
        print("\nTask not found!\n")

def change_status_ui(manager):
    print_menu("Changing Task Status")

    uuid = input("\nEnter UUID: ")

    print_menu("Set Status", [
        "Done",
        "Failed",
        "In process"
    ])

    try:
        choice = int(input("Choice: "))
    except ValueError:
        choice = 3

    status = {
        1: "Done",
        2: "Failed",
        3: "In process"
    }.get(choice, "In process")

    if manager.change_status(uuid, status):
        print("\nStatus changed.\n")
    else:
        print("\nTask not found!\n")

def change_priority_ui(manager):
    print_menu("Changing Task Priority")

    uuid = input("\nEnter UUID: ")

    print_menu("Set Priority", [
        "High",
        "Medium",
        "Low"
    ])

    try:
        choice = int(input("Choice: "))
    except ValueError:
        choice = 3

    priority = {
        1: "High",
        2: "Medium",
        3: "Low"
    }.get(choice, "Low")

    if manager.change_priority(uuid, priority):
        print("\nPriority changed.\n")
    else:
        print("\nTask not found!\n")

def change_description_ui(manager):
    print_menu("Changing Task Description")

    uuid = input("\nEnter UUID: ")

    description = input("\nNew description: ")

    if manager.change_description(uuid, description):
        print("\nDescription changed.\n")
    else:
        print("\nTask not found!\n")

def display_task_info(task: dict, index: int | None = None) -> None:
    if index is not None:
        print(f"{index}. UUID: {task['UUID']}")
    else:
        print(f"UUID: {task['UUID']}")

    print(f"Title: {task['Title']}")
    print(f"Description: {task['Description']}")
    print(f"Priority: {task['Priority']} (Weight: {task.get('Weight', 'N/A')})")
    print(f"Status: {task['Status']}\n")

def display_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("\nNo tasks found.\n")
        return

    for index, task in enumerate(tasks, start=1):
        display_task_info(task, index)