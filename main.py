import logic, user_choice


task_list = [] 
# ToDo: work with files that create/exist in 'storage.py' module.
"""this makes a logic error. because remove or don't save changes; 
Always makes the list empty. It's better first to check if the file is exist or not. and if
it doesn't, create one. then read from there and work with them. this way it's okay."""

while True:
    print("\n--Task Manager Menu--\n")
    print("1. Add task\n2. Remove task\n3. Change status\n4. Display tasks\n5. Display specific task\n6. Save\n7. Exit\n")
    #ToDo: before exiting, show a warning that tells do you want to save before exit? answers should be y or n
    user_choice.user_choice()


    title = input("Title: ")
    description = input("Description: ")
    task = logic.Task(title, description)
    task_list.append(task.info)