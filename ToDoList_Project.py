# ToDo : Fix creating file problem. Take help from Screenshots.

import csv
from tkinter import Tk, filedialog

"""
Import csv to work with csv files. We need to read and save changes of our ToDo List on a csv file.
CSV stands for Comma-Separated Value.

Import Tk and filedialog from tkinter package to take path directory and select file in a simple GUI.
GUI stands for Graphical User Interface
"""

task_list = []
high_priority_task_list = []
middle_priority_task_list = []
low_priority_task_list = []

"""
Define "task_list", "high_task_list", "middle_task_list" and "low_task_list" to keep values in continue.
The goal is to seperate tasks with different priority to sort our To Do list in high to low priority and know which task is 
more important to do first and which is not.

"high_priority_task_list" is a list of tasks with high priority.
"middle_priority_task_list" is a list of tasks with middle priority.
"low_priority_task_list" is a list of tasks with middle priority.
"""

class Task:
    def __init__(self, dict_name, task, description, priority):
        self.dict_name = dict_name
        self.task = task
        self.description = description
        self.priority = priority.capitalize()
        

"""
Define a class named "Task" with initial values: dict_name, task, description, priority. 

"dict_name" -- choose a name for the dictionary.
"task" -- what is your task
"description" -- Describe what is your task about and what you like to add as a note to remember.
"priority" -- Your task has a high, middle or low priority.
"""

class ToDoList(Task):
    def __init__(self, task, description, priority, dict_name):
        super().__init__(dict_name, task, description, priority)
        
        """
        a child class named "ToDoList" that inherited from its parent class named "Task".
        """
    def add_task(self):
            self.dict_name = {
                "task": self.task,
                "description": self.description,
                "priority": self.priority
                }
            """ 
            We define a dictionary with following keys:
                task - task's name
                description - describe what it is
                priority - what is the priority of this task? High - Middle or Low
            """

            if self.dict_name["priority"] in ("High", "Middle", "Low"):
                task_list.append(self.dict_name)
                return ("Your task added successfully. \u2705 \n")
            else:
                return ("Priority is not correct. \u274c")

            """
            If priority added correctly, task will append to the list.
            But the priority didn't recognize, will raise a message. 
            """
    
    @staticmethod           # used decorator here because don't need class's properties.
    def removing_task():
        remove_task = input("\U0001F5D1 Removing task - Enter task name: ")
        print()             # Blank line

        for task in task_list:
            if remove_task == task["task"]:
                task_list.remove(task)
                return ("Task removed \u2705 \n")
            
        return ("Not Found! \u274c \n")
    """
    define a removing function that takes task name and search for it in the list and delete it if found it.
    """

    @staticmethod
    def show_tasks():
        high_priority_task_list.clear()
        middle_priority_task_list.clear()  # This is actually correct, otherwise old data would accumulate. Keep these lines.
        low_priority_task_list.clear()
        
        for dict in task_list:

            if dict["priority"] == "High":
                high_priority_task_list.append(dict)

            elif dict["priority"] == "Middle":
                middle_priority_task_list.append(dict)
                
            elif dict["priority"] == "Low":
                low_priority_task_list.append(dict)

            else:
                print(f"Just use 'High, Middle or Low'. I can't accept {dict['priority']} as priority. \u274c \n")
        """
        An static function (decorated) that shows tasks in sorted priority from high to low

        ToDO: It need to be improved. I should make it better.
        """
        
        print("*** Your To Do List ***\n")
        print("First thing first - high priority: ")
        for dict in high_priority_task_list:
            print(f"\u2022 Task: {dict['task']}")
            print(f"    description: {dict['description']}\n")
        
        print("Middle priority: ")
        for dict in middle_priority_task_list:
            print(f"\u2022 Task: {dict['task']}")
            print(f"    description: {dict['description']}\n")
        
        print("Low priority: ")
        for dict in low_priority_task_list:
            print(f"\u2022 Task: {dict['task']}")
            print(f"    description: {dict['description']}\n")
        
        """
        After sorting priorities in seperated lists, in this part will prints and shows tasks in priority.
        """
    
    @staticmethod
    def choose_file():
        Tk().withdraw() # Hide the main window
        file_path = filedialog.askopenfilename()
        return file_path
    
    """
    Here using Tkinter package to work with GUI to choosing file
    """

    @staticmethod
    def where_to_save():
        root = Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(
            title="Select a Folder"
        )
        root.destroy()
        return folder_path
    
    """ 
    Also we used Tkinter package here because to be user friendly and easy to work with
    """


"""
Create file with "your favorite name".
You can change the file's name whenever you like:
"""
new_file = input("Do you want to create a new file? (y/n) -- ")

""" Asks for new file or working with old file """



if new_file.lower() in ("yes", "y"):

    file_name = input("Enter your favorite name --> ")
    your_to_do_list_name = file_name

    """ You can name your file whatever you like """
    
    try:
        path = ToDoList.where_to_save()
        with open(f"{your_to_do_list_name}.csv", "x"):
            pass
    except FileExistsError:
        print(f"\"{your_to_do_list_name}\" file is already exists.\n")
    else:
        print(f"\"{your_to_do_list_name}\".csv successfully created. \u2705 \n")
    
    """ Choose where you want to create and save your file """

    """ But if your chose to work with previous files, the following code will be executed. """
else:
    file = ToDoList.choose_file()
    with open("choosed_file", "a+"):
            
        process = True

        while process:
            print("1.Adding\n")
            print("2.Removing\n")
            print("3.Showing\n")
            print("4.Save & Quit\n")

            """ Main Panel """

            user_choice = int(input("Select: "))

            match user_choice:
                case 1:
                    user_task_name = input("Task: ")
                    user_task_description = input("Description: ")
                    print("\u26A0 Attention: I only accept 'High, Middle or Low' words as priority [I only care about words not write formatting].")
                    user_task_priority = input("Priority: ")
                    dict_name = user_task_name

                    """ In above, we take task information if user choose was 1 which means: 1.Adding """

                    task = ToDoList(user_task_name, user_task_description, user_task_priority, dict_name)
                    print(task.add_task())

                    with open(f"{ToDoList.choose_file()}", "a") as file:
                        writer = csv.DictWriter(file, fieldnames=["task", "description", "priority"])
                        if file.tell() == 0:
                            writer.writeheader()
                        writer.writerow(task.dict_name)

                    """ In here we used CSV package to save the results in a csv file """
                
                case 2:
                    print(ToDoList.removing_task())

                    """ This will removed """ 

                case 3:
                    ToDoList.show_tasks()

                    """ This will show the tasks """
                    
                case 4:
                    process = False

                    """ This will saves and stops the program """

                case _:
                    print("\u274c Unexpected. Try again!")

                    """ This note will prints if the user enters the incorrect input """