import uuid
from .storage import write_json_file

class Task:
    def __init__(self):
        self.uuid = None 
        self.title = None
        self.description = None
        self.priority = None
        self.status = "In process"       # for all instances
        self.dict = None # returns a dict

    def set_uuid(self):
        return str(uuid.uuid4())

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

class TaskManager:
    def __init__(self, task_list):
        self.task_list = task_list
    
    @staticmethod
    def task_uuid(task_list):
        """
        Checks if a specific uuid exists in the task_list
        Returns: (bool, dict_element)
        """
        input_uuid = input("\nEnter UUID: ")
        for dict_element in task_list:
            if dict_element["UUID"] == input_uuid:
                return True, dict_element
        return False, None

    def add_task(self):
        task = Task()
        task.uuid = task.set_uuid()
        task.title = input("\nTitle:")
        task.description = input("\nDescription: ")
        task.priority = task.set_priority()
        task.dict = task.to_dict() # return a dictionary
        self.task_list.append(task.dict)
        print("\nNew task added successfully.")
        

    def remove_task(self): # search via uuid
        """
        task_uuid function checks every single element in task_list that entered uuid is 
        the same with that specific uuid or not; 
        Then returns True or False;
        """
        uuid_status, dict_element = self.task_uuid(self.task_list) 
        if uuid_status:
            self.task_list.remove(dict_element)
            print("\nTask removed.\n")
        else:
            print("\nNot found!\n")

    def change_status(self): # Changing 'Status' from "In process" to "Done"
        uuid_status, dict_element = self.task_uuid(self.task_list)
        if uuid_status:
            input_user_status = input("\nEnter status: ")
            dict_element["Status"] = input_user_status
            print(f"\nStatus changed successfully to \"{input_user_status}\".\n")
        else:
            print("\nNot found!\n")  

    def change_priority(self):
        uuid_status, dict_element = self.task_uuid(self.task_list)
        if uuid_status:
            task = Task()
            dict_element["Priority"] = task.set_priority()
            print("\n'Priority' changed successfully!\n")
        else:
            print("\nNot found!\n")

    def show_task(self): # show an specific task via uuid
        uuid_status, dict_element = self.task_uuid(self.task_list)
        if uuid_status:
            print(f"\n{dict_element}\n")
        else:
            print("\nNot found!\n")

    def display(self): # show all tasks
        if not self.task_list: # check is empty
            print("\nNo tasks available. \n")
        else:
            for element in self.task_list:
                print(f"{element}\n")
            print("\n-- End of tasks --")

    def display_only_Done(self):
        done_list = []
        for task in self.task_list:
            if task["Status"] == "Done":
                done_list.append(task)
        for task in done_list:
            print(task, "\n")

    def display_only_Not_Done(self):
        Not_Done_list = []
        for task in self.task_list:
            if task["Status"] != "Done" and task["Status"] != "Failed":
                Not_Done_list.append(task)
        for task in Not_Done_list:
            print(task, "\n")

    def sort_by_priority_and_display(self, json_file):
        sort_list = []
        high_list = []
        medium_list = []
        low_list = []
        for task in self.task_list:
            if task["Priority"] == "High":
                high_list.append(task)
            elif task["Priority"] == "Medium":
                medium_list.append(task)
            elif task["Priority"] == "Low":
                low_list.append(task)
        sort_list.extend(high_list)
        sort_list.extend(medium_list)
        sort_list.extend(low_list)
        for task in sort_list:
            print(task,"\n")
        self.task_list = sort_list
        self.save(json_file)

    def save(self, json_file): # dump in json file
        write_json_file(json_file, self.task_list)
        print("\nSaved successfully.\n")
    
    def exit(self, json_file):
        print("\n1. Save changes\n")
        print("2. Discard Changes\n")
        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid Value\n")
        else:
            if user_select == 1:
                print("Saving changes...")
                self.save(json_file)
                return False
                
            elif user_select == 2:
                print("Exit 'WITHOUT' saving changes\n")
                return False

            else:
                print("\nInvalid Value\n")
