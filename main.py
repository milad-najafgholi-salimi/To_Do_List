from common import task_list, json_file
from storage import check_selection, JsonOperation
from selection import user_choice

while True:
    print("\n --Main Menu--\n")
    print("1. Open existing file\n2. Create new file\n3. Quit\n")
    try:
        user_select = int(input("Select: "))
    except ValueError:
        print("\nInvalid value\n")
        break
    else:
        json_file = check_selection(user_select) # path of json file (include: directory path + file)
    
    if json_file != False and user_select == 1:
        while True:
            print("\n--Task Manager Menu--\n")
            print("1. Add task\n2. Remove task\n3. Change status\n4. Display tasks\n5. Display specific task\n6. Save\n7. Exit\n")

            dict_data = JsonOperation.read_json_file(json_file)
            """
            To avoid appending a list into a list (nested list), use extend method.
            This way, the output will be just a list with elements inside it.
            """
            task_list.extend(dict_data)
            user_choice()

    elif json_file == False:
        break