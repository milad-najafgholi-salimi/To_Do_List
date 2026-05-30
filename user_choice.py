from logic import TaskManager

def user_choice():
        try:
            usr_select = int(input("Select: "))
            if usr_select in range(1,8):
                match usr_select:
                      case 1:
                            TaskManager.add_task()
                      case 2:
                            TaskManager.remove_task()
                      case 3:
                            TaskManager.change_status()
                      case 4:
                            TaskManager.display() # show all tasks
                      case 5:
                            TaskManager.show_task() # show an specific task
                      case 6:
                            TaskManager.save() # ToDo: need to save changes in a json file via storage.py module - Add a function for saving
                      case 7:
                            TaskManager.exit() # ToDo: add a function in storage.py module for asking 'save changes' or 'discard changes'
                                                # if user choose 'save changes', save function call and run. and if user choose 'discard changes' just break without doing anything
            else:
                print("Invalid value\n")
                return False # in 'main.py' module, the while loop will break.
        except ValueError:
                print("Invalid value\n")
                return False  # in 'main.py' module, the while loop will break.
