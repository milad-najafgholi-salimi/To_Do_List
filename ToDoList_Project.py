# My simple To Do List project

import csv


task_list = []
high_task_list = []
middle_task_list = []
low_task_list = []


class Task:
    def __init__(self, task, description, priority, dict_name):
        self.task = task
        self.description = description
        self.priority = priority.capitalize()
        self.dict_name = dict_name


class ToDoList(Task):
    def __init__(self, task, description, priority, dict_name):
        super().__init__(task, description, priority, dict_name)

    def adding_task(self):
            self.dict_name = {
                "task": self.task,
                "description": self.description,
                "priority": self.priority
                }
            if self.dict_name["priority"] in ["High", "Middle", "Low"]:
                task_list.append(self.dict_name)
                return ("Your task added successfully. \u2705 \n")
            else:
                return ("Priority is not correct. \u274c")
    
    @staticmethod
    def removing_task():
        remove_task = input("\U0001F5D1 Removing task - Enter task name: ")
        print("")

        for task in task_list:
            if remove_task == task["task"]:
                task_list.remove(task)
                return ("Task removed \u2705 \n")
            
        return ("Not Found! \u274c \n")
    
    @staticmethod
    def showing_tasks():
        high_task_list.clear()
        middle_task_list.clear()
        low_task_list.clear()
        
        for dict in task_list:

            if dict["priority"] == "High":
                high_task_list.append(dict)

            elif dict["priority"] == "Middle":
                middle_task_list.append(dict)
                
            elif dict["priority"] == "Low":
                low_task_list.append(dict)

            else:
                print(f"Just use 'High, Middle or Low'. I can't accept {dict["priority"]} as priority. \u274c \n")
        
        print("***Your To Do List in Priority***\n")
        print("First thing first - high priority: ")
        for dict in high_task_list:
            print(f"\u2022 Task: {dict["task"]}")
            print(f"    description: {dict["description"]}\n")
        
        print("Middle priority: ")
        for dict in middle_task_list:
            print(f"\u2022 Task: {dict["task"]}")
            print(f"    description: {dict["description"]}\n")
        
        print("Low priority: ")
        for dict in low_task_list:
            print(f"\u2022 Task: {dict["task"]}")
            print(f"    description: {dict["description"]}\n")


# Creating file with "your optional" name

# You can change the name of file what ever you like:
your_to_do_list_name = "To-Do-List-file"

# Creating file if it doesn't exist.
try:
    with open(f"D:\{your_to_do_list_name}.csv", "x"):
        pass
except FileExistsError:
    print("The specific file is already exists.\n")
else:
    print(f"{your_to_do_list_name}.csv successfully created. \u2705 \n")


# Opening file and Starting to work:
with open(f"D:\{your_to_do_list_name}.csv", "a+") as file:

    process = True

    while process:
        print("1.Adding\n")
        print("2.Removing\n")
        print("3.Showing\n")
        print("4.Save & Quit\n")

        user_choose = int(input("Your command: "))

        match user_choose:
            case 1:
                task_name = input("Task: ")
                my_task_description = input("Description: ")
                print("\u26A0 Attention: I only accept 'High, Middle or Low' words as priority [I only care about words not write formatting].")
                my_task_priority = input("Priority: ")
                dict_name = task_name

                task = ToDoList(task_name, my_task_description, my_task_priority, dict_name)
                print(task.adding_task())
                with open(f"D:\{your_to_do_list_name}.csv", "a") as file:
                    writer = csv.DictWriter(file, fieldnames=["task", "description", "priority"])
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow(task.dict_name)
                print("")

            case 2:
                print(ToDoList.removing_task())

            case 3:
                ToDoList.showing_tasks()
                
            case 4:
                process = False

            case _:
                print("\u274c Unexcepted. Try again!")
