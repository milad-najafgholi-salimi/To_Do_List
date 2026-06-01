import uuid
# from storage import JsonOperation
from main import task_list
from selection import task_uuid

"""
"We use classes because, for example, when we create an object called 'Language', we can store 
tasks for English, French, and Persian that need to be completed. We assign each task a title, 
description, and priority. 
This keeps them categorized and well-organized.""
"""

class Task:
    def __init__(self, title: str, description: str):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = self.set_priority()
        self.status = "In process"       # for all instances
        self.info = self.to_dict() # returns a dict

    def set_priority(self) -> str:
        print("\n--Set priority--\n")
        print("1.High\n2.Medium\n3.Low\n")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input\nsetting to Default (3.Low)\n")
            return "Low"
        else:
            if choice in (1, 2, 3):
                match choice:
                    case 1:
                        return "High"
                    case 2:
                        return "Medium"
                    case 3:
                        return "Low"
            else:
                print("\nOut of range! setting to Default (3.Low)\n")
                return "Low"
        

    def to_dict(self) -> dict:
        return {
            "UUID": self.uuid,
            "Title": self.title,
            "Description": self.description,
            "Priority": self.priority,
            "Status": self.status
        }
    
class TaskManager(Task):
    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        task = Task(title, description)
        data = task.info
        task_list.append(data)
        print("New task added successfully.")
        

    def remove_task(self): # search via uuid
        """
        task_uuid function checks every single element in task_list that entered uuid is 
        the same with that specific uuid or not; 
        Then returns True or False;
        """
        uuid_status, dict_element = task_uuid() 
        if uuid_status:
            del dict_element
            print("\nTask removed.\n")
        else:
            print("\nNot found!\n")

    def change_status(): # Changing 'Status' from "In process" to "Done"
        uuid_status, dict_element = task_uuid()
        if uuid_status:
            dict_element["Status"] = "Done"
            print("\nStatus changed successfully from \"In process\" to \"Done. \"\n")
        else:
            print("\nNot found!\n")  

    def show_task(): # show an specific task via uuid
        uuid_status, dict_element = task_uuid()
        if uuid_status:
            print("\n" + dict_element + "\n")
        else:
            print("\nNot found!\n")

    def display(): # show all tasks
        for element in task_list:
            print(element + "\n")
        print("\n Done!")

    def save(): # dump in json file
        pass
    
    def exit(): # ask for save or discard - save: dump to json file | discard: break 
        pass
