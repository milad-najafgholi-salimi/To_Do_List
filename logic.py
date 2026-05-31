import uuid
from storage import JsonOperation
from main import task_list
# from user_choice import user_choice

"""
"We use classes because, for example, when we create an object called 'Language', we can store 
tasks for English, French, and Persian that need to be completed. We assign each task a title, 
description, and priority. 
This keeps them categorized and well-organized.""
"""

class Task:
    def __init__(self, title: str, description: str):
        self.uuid = uuid.uuid4()
        self.title = title
        self.description = description
        self.priority = self.set_priority()
        self.state = "In process"       # for all instances
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
            "State": self.state
        }
    
class TaskManager(Task):
    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        task = Task(title, description)
        data = task.info
        task_list.append(data)
        

    def remove_task(self): # search via uuid
        pass

    def change_status(): # from in process to Done
        pass

    def display(): # show all tasks
        pass

    def show_task(): # show an specific task:  parameter --> uuid
        pass

    def save(): # dump in json file
        pass
    
    def exit(): # ask for save or discard - save: dump to json file | discard: break 
        pass
