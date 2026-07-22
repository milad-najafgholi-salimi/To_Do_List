from .storage import check_selection, read_json_file
from .logic import TaskManager
from .ui import print_menu, clear_screen, wait_for_user

def task_manager_menu(manager: TaskManager, json_file: str) -> None:
    """
    We used lambda functions to avoid immediate execution of the save method when 
    it is called from the actions dictionary.
    If we didn't use lambda, the method would be executed immediately when the 
    dictionary is created,
    which is not the desired behavior. By using lambda, we ensure that the method is 
    only executed when the corresponding user choice is selected.
    """
    actions = {
        1: manager.add_task,
        2: manager.remove_task,
        3: manager.change_status,
        4: manager.change_priority,
        5: manager.change_description,
        7: manager.show_task,
        8: lambda: manager.save(json_file),
    }

    # Task Manager Menu Loop
    while True:
        clear_screen()

        print_menu("TASK MANAGER", [
        "Add task",
        "Remove task",
        "Change status",
        "Change priority",
        "Change description",
        "Display tasks",
        "Display specific task",
        "Save",
        "Save & Exit",
    ],
)
        
        try:
            user_choice = int(input("Select: "))
        except ValueError:
            print("\nInvalid value\n")
            continue

        if user_choice in actions:
            actions[user_choice]()
            wait_for_user()

        elif user_choice == 6:
            print_menu("DISPLAY TASKS", [
                "All",
                'Only "Done"',
                'Only "Not Done"',
                'Only "Failed"',
                "Sort by Priority & Status"
                ]
            )
            
            try:
                select = int(input("Select: "))
            except ValueError:
                print("\nInvalid value\n")
                wait_for_user()
                continue

            match select:
                case 1:
                    manager.display_tasks()
                case 2:
                    manager.display_only_done()
                case 3:
                    manager.display_only_in_process()
                case 4:
                    manager.display_only_failed()
                case 5:
                    manager.sort_by_priority_and_display()
                case _:
                    print("\nInvalid Value!\n")
            
            wait_for_user()

        elif user_choice == 9:
            if manager.exit_menu(json_file):
                break

        else:
            print("\nInvalid value\n")
            wait_for_user()


def main():
    # Main Menu
    while True:
        clear_screen()

        print_menu("MAIN MENU", ["Open existing file", "Create new file", "Quit"])

        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid value\n")
            wait_for_user()
            continue
        
        json_file = check_selection(user_select) # json_file: directory/file.json

        if json_file is False:
            break
        elif user_select == 3:
            break

        elif user_select in (1, 2):
            task_dict = {}
            # Load existing data if file exists and has content
            data = read_json_file(json_file) # data is a list with dictionary elements.
            if data:
                for task in data:
                    """
                    :data: list
                    :task: dictionary
                    :task["UUID"]: return UUID Value via UUID Key 

                    Add to task_dict Dictionary:
                    task_dict[UUID as string] = task as a dictionary
                    
                    Output is like:
                    {UUID_A: {task_A}, UUID_B: {task_B}}
                    """
                    task_dict[task["UUID"]] = task
            
            # Create TaskManager instance with the task_dict
            manager = TaskManager(task_dict)

            task_manager_menu(manager, json_file)
            
if __name__ == "__main__":
    main()