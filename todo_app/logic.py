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
    def __init__(self, task_dict):
        self.task_dict = task_dict
    
    @staticmethod
    def task_uuid(task_dict):
        """
        Checks if a specific uuid exists in the task_dict
        Returns: (bool, dict_element)
        """
        input_uuid = input("\nEnter UUID: ")
        if input_uuid in task_dict:
            return True, task_dict[input_uuid]
        return False, None

    def add_task(self):
        task = Task()
        task.uuid = task.set_uuid()
        task.title = input("\nTitle: ")
        task.description = input("\nDescription: ")
        task.priority = task.set_priority()
        task.dict = task.to_dict() # return an organized dictionary
        self.task_dict[task.uuid] = task.dict
        print("\nNew task added successfully.")
        

    def remove_task(self): # search via uuid
        uuid_status, dict_element = self.task_uuid(self.task_dict) 
        if uuid_status:
            del self.task_dict[dict_element["UUID"]]
            print("\nTask removed.\n")
        else:
            print("\nNot found!\n")

    def change_status(self): # Changing 'Status' from "In process" to whatever you want
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            input_user_status = input("\nEnter status: ")
            dict_element["Status"] = input_user_status
            print(f"\nStatus changed successfully to \"{input_user_status}\".\n")
        else:
            print("\nNot found!\n")  

    def change_priority(self):
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            task = Task()
            dict_element["Priority"] = task.set_priority()
            print("\n'Priority' changed successfully!\n")
        else:
            print("\nNot found!\n")

    def show_task(self): # show an specific task via uuid
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            print(f"\n{dict_element}\n")
        else:
            print("\nNot found!\n")

    def display_tasks(self): # show all tasks
        if not self.task_dict: # check is empty
            print("\nNo tasks available. \n")
        else:
            print("\n-- Start of tasks --\n")
            for element in self.task_dict.values(): # Returns all values without keys
                print(f"{element}\n")
            print("\n-- End of tasks --\n")

    def display_only_Done(self):
        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] == "Done":
                print(task, "\n")

    def display_only_in_process(self):
        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] != "Done" and task["Status"] != "Failed":
                print(task, "\n")

    def display_only_failed(self):
        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] == "Failed":
                print(task, "\n")

    def sort_by_priority_and_display(self, json_file):
        All_sort_list = []
        Done_list = []
        In_Process_list = []
        Failed_list = []
        Other_list = []

        for task in self.task_dict.values():
            if task["Status"] == "Done":
                Done_list.append(task)
            elif task["Status"] == "In process":
                In_Process_list.append(task)
            elif task["Status"] == "Failed":
                Failed_list.append(task)
            else:
                Other_list.append(task)

        sorted_Done_tasks = self.sort_priority(Done_list)
        sorted_In_Process_tasks = self.sort_priority(In_Process_list)
        sorted_Failed_tasks = self.sort_priority(Failed_list)
        sorted_Other_tasks = self.sort_priority(Other_list)

        All_sort_list.extend(sorted_Done_tasks)
        All_sort_list.extend(sorted_In_Process_tasks)
        All_sort_list.extend(sorted_Failed_tasks)
        All_sort_list.extend(sorted_Other_tasks)

        for task in All_sort_list:
            print(task, "\n")
            
        self.save(json_file, All_sort_list)

    def sort_priority(self, List: list) -> list:
        sorted_list = []
        high_list = []
        medium_list = []
        low_list = []
        for task in List:
            if task["Priority"] == "High":
                high_list.append(task)
            elif task["Priority"] == "Medium":
                medium_list.append(task)
            elif task["Priority"] == "Low":
                low_list.append(task)

        sorted_list.extend(high_list)
        sorted_list.extend(medium_list)
        sorted_list.extend(low_list)
        return sorted_list

    def save(self, json_file, task_list = None): # dump in json file
        if task_list is None:
            task_list = list(self.task_dict.values())
        write_json_file(json_file, task_list)
        # Updating task_dict via task_list
        self.task_dict = {task["UUID"]: task for task in task_list}
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
