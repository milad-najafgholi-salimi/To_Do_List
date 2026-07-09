import uuid
from .storage import write_json_file, read_json_file

class Task:
    # Weighted Average - Every task by it's priority, have different weights
    # It's a constant so we used upper-case form
    PRIORITY_WEIGHTS = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    def __init__(self):
        self.uuid = None 
        self.title = None
        self.description = None
        self.priority = None
        self.status = "In process"  # for all instances
        self.dict = None   # returns a dict
        self.weight = None

    def set_uuid(self):
        return str(uuid.uuid4())

    def set_priority(self) -> str:
        print("\n--Set priority--\n")
        print("1.High\n2.Medium\n3.Low\n")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input\nsetting to Default (3.Low)\n")
            priority = "Low"
            self.weight = self.PRIORITY_WEIGHTS[priority] 
            return priority
        else:
            if choice in (1, 2, 3):
                match choice:
                    case 1:
                        priority = "High"
                    case 2:
                        priority = "Medium"
                    case 3:
                        priority = "Low"
                self.weight = self.PRIORITY_WEIGHTS[priority]
                return priority
            else:
                print("\nOut of range! setting to Default (3.Low)\n")
                priority = "Low"
                self.weight = self.PRIORITY_WEIGHTS[priority]
                return priority
        

    def to_dict(self) -> dict:
        return {
            "UUID": self.uuid,
            "Title": self.title,
            "Description": self.description,
            "Priority": self.priority,
            "Weight": self.weight,
            "Status": self.status
        }

class TaskManager:
    def __init__(self, task_dict):
        self.task_dict = task_dict

    @staticmethod
    def task_uuid(task_dict):
        """
        Checks if a specific uuid exists in the task_dict
        Return: (bool, dict_element)
        """
        input_uuid = input("\nEnter UUID: ")
        if input_uuid in task_dict:
            return True, task_dict[input_uuid] # :task_dict[input_uuid]: Returns {task} - as value - UUID_key: {task}_value
        return False, None

    def add_task(self) -> None:
        task = Task()
        task.uuid = task.set_uuid()
        print("\n" + "="*50)
        print("--- Adding New Task ---")
        print("="*50)
        task.title = input("\nTitle: ")
        task.description = input("\nDescription: ")
        task.priority = task.set_priority()
        task.dict = task.to_dict() # return an organized dictionary
        self.task_dict[task.uuid] = task.dict # Add new key-value pair to task_dict
        print("\nNew task added successfully.")
        print("\n" + "="*50 + "\n")


    def remove_task(self) -> None: # search via uuid
        print("\n" + "="*50)
        print("--- Removing a Task ---")
        print("="*50)
        uuid_status, dict_element = self.task_uuid(self.task_dict) 
        if uuid_status:
            del self.task_dict[dict_element["UUID"]]
            print("\nTask removed.\n")
        else:
            print("\nNot found!\n")
        print("="*50 + "\n")

    def change_status(self): # Changing 'Status' from "In process" to whatever you want
        print("\n" + "="*50)
        print("--- Changing a Task Status ---")
        print("="*50)
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            input_user_status = input("\nEnter status: ")
            dict_element["Status"] = input_user_status
            print(f"\nStatus changed successfully to \"{input_user_status}\".\n")
        else:
            print("\nNot found!\n")
        print("="*50 + "\n")

    def change_priority(self):
        print("\n" + "="*50)
        print("--- Changing a Task Priority ---")
        print("="*50)
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            task = Task()
            dict_element["Priority"] = task.set_priority()
            dict_element["Weight"] = task.weight
            print("\n'Priority' changed successfully!\n")
        else:
            print("\nNot found!\n")
        print("="*50 + "\n")

    def show_task(self): # show an specific task via uuid
        print("\n" + "="*50)
        print("--- Display an Specific Task ---")
        print("="*50)
        uuid_status, dict_element = self.task_uuid(self.task_dict)
        if uuid_status:
            print(f"\nUUID: {dict_element['UUID']}")
            print(f"Title: {dict_element['Title']}")
            print(f"Description: {dict_element['Description']}")
            print(f"Priority: {dict_element['Priority']} (Weight: {dict_element.get('Weight', 'N/A')})")
            print(f"Status: {dict_element['Status']}\n")
        else:
            print("\nNot found!\n")
        print("="*50 + "\n")

    def display_tasks(self) -> None: # show all tasks
        if not self.task_dict: # check is empty
            print("\nNo tasks available. \n")
        else:
            index = 1
            for element in self.task_dict.values(): # Returns all values without keys
                print(f"{index}. UUID: {element['UUID']}")
                print(f"    Title: {element['Title']}")
                print(f"    Description: {element['Description']}")
                print(f"    Priority: {element['Priority']} (Weight: {element.get('Weight', 'N/A')})")
                print(f"    Status: {element['Status']}\n")
                index += 1
            print("-"*50 + "\n")
            self.report(list(self.task_dict.values()))

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

    def sort_by_priority_and_display(self):
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

        # Updating task_dict via All_sort_list
        self.task_dict = {task["UUID"]: task for task in All_sort_list}

        index = 1
        for task in All_sort_list:
            print(f"{index}. UUID: {task['UUID']}")
            print(f"    Title: {task['Title']}")
            print(f"    Description: {task['Description']}")
            print(f"    Priority: {task['Priority']} (Weight: {task.get('Weight', 'N/A')})")
            print(f"    Status: {task['Status']}\n")
            index += 1

        print("-"*50 + "\n")
        self.report(list(self.task_dict.values()))

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
    
    def report(self, data: list) -> dict: 
        """
        Generates a report with statistics and grade based on task completion.

        :data: list with dict element

        if data was empty, returns an empty list; But if data wasn't emtpy,
        returns a list with dictionary elements.
        Example: [{...: ...}, {...: ...}, ...]
        """
        if not data: # Runs only if data is an empty list
            print("\nNothing to calculate!\n")
            return {}
        
        total_tasks = len(data)
        done_counter = 0
        failed_counter = 0
        in_process_counter = 0
        total_weight = 0

        for task in data:
            """
            Why we used `.get` method? Because:
            1) Tries to find the key "Status" in the task dictionary
            2) If found: returns the value associated with "Status"
            3) If NOT found: returns the default value "Unknown" instead of raising an error

            with this, we avoid getting errors if:
            - User edits file manually and delete the key.
            - Newer version doesn't support key.
            - JSON file is corrupted or data missed.
            - Possible bugs. 
            """
            status = task.get("Status", "Unknown")
            weight = task.get("Weight", 0)
            total_weight += weight
            if status == "Done":
                done_counter += 1
            elif status == "Failed":
                failed_counter += 1
            elif status == "In process":
                in_process_counter += 1
        
        done_weight = sum(task.get("Weight", 0) for task in data if task.get("Status") == "Done")

        done_percentage = (done_counter / total_tasks) * 100 if total_tasks > 0 else 0
        not_done_count = total_tasks - done_counter
        not_done_percentage = (not_done_count / total_tasks) * 100 if total_tasks > 0 else 0
        failed_percentage = (failed_counter / total_tasks) * 100 if total_tasks > 0 else 0
        in_process_percentage = (in_process_counter / total_tasks) * 100 if total_tasks > 0 else 0

        weight_done_percentage = (done_weight / total_weight * 100) if total_weight > 0 else 0

        if weight_done_percentage >= 90:
            grade = "A"
            grade_description = "Excellent"
        elif weight_done_percentage >= 80:
            grade = "B"
            grade_description = "Very Good"
        elif weight_done_percentage >= 70:
            grade = "C"
            grade_description = "Good but try harder"
        elif weight_done_percentage >= 60:
            grade = "D"
            grade_description = "Not good - Try harder"
        else:
            grade = "F"
            grade_description = "Awefull - what the fuck is this?"

        report = {
            "Total Tasks": total_tasks,
            "Total Weight": total_weight,
            "Tasks Done": done_counter,
            "Weight of Done Tasks": done_weight,
            "Weighted Done Percentage": f"{weight_done_percentage:.2f}%",
            "Tasks Not Done": not_done_count,
            "Tasks Failed": failed_counter,
            "Tasks In Process": in_process_counter,
            "Done Percentage": f"{done_percentage:.2f}%",
            "Not Done Percentage": f"{not_done_percentage:.2f}%",
            "Failed Percentage": f"{failed_percentage:.2f}%",
            "In Process Percentage": f"{in_process_percentage:.2f}%",
            "Grade": grade,
            "Grade Description": grade_description
        }
        
        # Display Report
        print("\n" + "="*50)
        print("Task Completion Report")
        print("="*50)
        for key, value in report.items():
            print(f"{key}: {value}")
        print("="*50 + "\n")
        
        return report

    def save(self, json_file, task_list = None): # dump in json file
        if task_list is None:
            task_list = list(self.task_dict.values())
        
        # Updating task_dict via task_list
        self.task_dict = {task["UUID"]: task for task in task_list}

        # Save changes on Tasks file
        write_json_file(json_file, task_list)
        print(f"\nTasks file Saved to: {json_file}\n")

        # Save Report in a separated JSON file
        """
        :report_dict_data: dictionary
        :[report_dict_data]: this way, we make it a list - a list with one element which is a dictionary -
        Because write_json_file() function expects a list NOT a dictionary.
        """
        report_dict_data = self.report(task_list)
        """
        To understand code below better:
            filename = "tasks.json"
            new_filename = filename.replace(".json", "_report.json")
            print(new_filename)  # Output: "tasks_report.json"
        """
        report_file = json_file.replace(".json", "_report.json") 
        write_json_file(report_file, [report_dict_data])
        print(f"Report file saved to: {report_file}\n")


    def exit(self, json_file):
        print("\n1. Save changes\n")
        print("2. Discard Changes\n")
        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid Value\n")
            return True
        if user_select == 1:
            self.save(json_file)
            return False
        elif user_select == 2:
            print("Exit 'WITHOUT' saving changes\n")
            return False
        else:
            print("\nInvalid Value\n")
            return True
