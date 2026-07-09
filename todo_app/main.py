from .storage import check_selection, read_json_file
from .logic import TaskManager

def main():
    while True:
        print("\n --Main Menu--\n")
        print("1. Open existing file\n")
        print("2. Create new file\n")
        print("3. Quit\n")

        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid value\n")
            continue
        
        json_file = check_selection(user_select) # json_file: directory/file.json

        if json_file is False:
            break
        elif user_select == 3:
            break

        elif user_select == 1 or user_select == 2:
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
            
            # Task Manager Menu Loop
            while True:
                print("\n--Task Manager Menu--\n")
                print("1. Add task\n")
                print("2. Remove task\n")
                print("3. Change status\n")
                print("4. Change priority\n")
                print("5. Display tasks\n")
                print("6. Display specific task\n")
                print("7. Save\n")
                print("8. Save & Exit\n")
                
                try:
                    user_choice = int(input("Select: "))
                except ValueError:
                    print("\nInvalid value\n")
                    continue
                
                if user_choice == 1:
                    manager.add_task()

                elif user_choice == 2:
                    manager.remove_task()

                elif user_choice == 3:
                    manager.change_status()

                elif user_choice == 4:
                    manager.change_priority()

                elif user_choice == 5:
                    print("\n-- Display Tasks --\n")
                    print("1. All")
                    print("2. Only \"Done\"")
                    print("3. Only \"Not Done\"")
                    print("4. Only \"Failed\"")
                    print("5. Display & Sort tasks by 'priority' & 'status'\n")
                    try:
                        select = int(input("Select: "))
                    except ValueError:
                        print("\nInvalid value\n")
                        continue
                    match select:
                        case 1:
                            manager.display_tasks()
                        case 2:
                            manager.display_only_Done()
                        case 3:
                            manager.display_only_in_process()
                        case 4:
                            manager.display_only_failed()
                        case 5:
                            manager.sort_by_priority_and_display()
                        case _:
                            print("\nInvalid Value!\n")

                elif user_choice == 6:
                    manager.show_task()

                elif user_choice == 7:
                    manager.save(json_file)

                elif user_choice == 8:
                    result = manager.exit(json_file)
                    if result == False:
                        break

                else:
                    print("\nInvalid value\n")
        else:
            print("\nInvalid value\n")

if __name__ == "__main__":
    main()