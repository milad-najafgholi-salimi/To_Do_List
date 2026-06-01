from selection import user_choice
# from logic import Task
from storage import check_selection, JsonOperation


task_list = [] 
"""this makes a logic error. because remove or don't save changes; 
Always makes the list empty. It's better first to check if the file is exist or not. and if
it doesn't, create one. then read from there and work with them. this way it's okay."""

while True:
    print("\n --Main Menu--\n")
    print("1. Open existing file\n 2. Create new file\n")
    try:
        user_select = int(input("Select: "))
    except ValueError:
        print("\nInvalid value\n")
        break
    else:
        json_file = check_selection(user_select) # path of json file (include: directory path + file)


    print("\n--Task Manager Menu--\n")
    print("1. Add task\n2. Remove task\n3. Change status\n4. Display tasks\n5. Display specific task\n6. Save\n7. Exit\n")
    #ToDo: before exiting, show a warning that tells do you want to save before exit? answers should be y or n
    
    dict_data = JsonOperation.read_json_file(json_file)
    task_list.append(dict_data)
    user_choice()
