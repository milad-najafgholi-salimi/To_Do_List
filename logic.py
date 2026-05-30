import uuid
from user_choice import user_choice

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
        self.info = self.to_dict()

    def set_priority(self) -> str:
        print("\n--Set priority--\n")
        print("1.High\n2.Medium\n3.Low\n")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice in (1, 2, 3):
                match choice:
                    case 1:
                        return "High"
                    case 2:
                        return "Medium"
                    case 3:
                        return "Low"
            else:
                print("Out of range! setting to Default (3.Low)")
                return "Low"
        except ValueError:
            print("Invalid input\nsetting to Default (3.Low)\n")
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
        pass

    def remove_task(self):
        pass

    def change_status():
        pass

    def display():
        pass

    def show_task(): # parameter --> uuid
        pass

    def save():
        pass
    
    def exit():
        pass
