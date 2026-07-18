import uuid
from .storage import write_json_file
from .ui import print_menu

class Task:
    # Weighted Average - Every task by it's priority, have different weights
    # It's a constant so we used upper-case form
    PRIORITY_WEIGHTS = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    def __init__(self, title: str, description: str, priority: str, status: str = "In process"):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.weight = self.PRIORITY_WEIGHTS[priority]

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

    def get_task_by_uuid(self) -> dict | None:
        input_uuid = input("\nEnter UUID: ")

        return self.task_dict.get(input_uuid)
    
    def get_selected_task(self) -> dict | None:
        task = self.get_task_by_uuid()

        if task is None:
            print("\nTask not found!\n")
        
        return task
    
    def get_priority(self) -> str:
        print_menu("Set Priority", ["High", "Medium", "Low"])

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input.")
            print("Setting to default: Low\n")
            return "Low"

        match choice:
            case 1:
                return "High"
            case 2:
                return "Medium"
            case 3:
                return "Low"
            case _:
                print("\nOut of range!")
                print("Setting to default: Low\n")
                return "Low"

    def get_status(self) -> str:
        print_menu("Set Status", ["Done", "Failed", "In process"])

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input.")
            print("Setting to default: In process\n")
            return "In process"
        
        match choice:
            case 1:
                return "Done"
            case 2:
                return "Failed"
            case 3:
                return "In process"
            case _:
                print("\nOut of range!")
                print("Setting to default: In process\n")
                return "In process"

    def get_description(self) -> str:
        return input("\nSet new description: ")

    def display_task_info(self, task: dict, index: int | None = None) -> None:
        if index is not None:
            print(f"{index}. UUID: {task['UUID']}")
        else:
            print(f"UUID: {task['UUID']}")

        print(f"Title: {task['Title']}")
        print(f"Description: {task['Description']}")
        print(f"Priority: {task['Priority']} (Weight: {task.get('Weight', 'N/A')})")
        print(f"Status: {task['Status']}\n")

    def add_task(self) -> None:
        print_menu("Adding Task")

        title = input("\nTitle: ")
        description = input("\nDescription: ")

        priority = self.get_priority()

        task = Task(title=title, description=description, priority=priority)

        self.task_dict[task.uuid] = task.to_dict()
        
        print("\nNew task added successfully.")

    def remove_task(self) -> None: # search via uuid
        print_menu("Removing a Task")

        task = self.get_selected_task()

        if task is None:
            return
        
        del self.task_dict[task["UUID"]]

        print("\nTask removed.\n")

    def change_status(self):
        print_menu("Changing a Task Status")
        task = self.get_selected_task()

        if task is None:
            return
        
        status = self.get_status()
        task["Status"] = status

        print(f"\nStatus changed successfully to '{status}'.\n")

    def change_priority(self):
        print_menu("Changing a Task Priority")

        task = self.get_selected_task()

        if task is None:
            return
        
        priority = self.get_priority()

        task["Priority"] = priority
        task["Weight"] = Task.PRIORITY_WEIGHTS[priority]

        print("\nPriority changed successfully!\n")

    def change_description(self):
        print_menu("Changing a Task Description")

        task = self.get_selected_task()

        if task is None:
            return
        
        description = self.get_description()
        task["Description"] = description

        print("\nDescription changed successfully!\n")

    def show_task(self): # show an specific task via uuid
        print_menu("Displaying a Specific Task")

        task = self.get_selected_task()

        if task is None:
            return
        
        self.display_task_info(task)

    def display_tasks(self) -> None:
        print_menu("Displaying Tasks")

        if not self.task_dict:
            print("\nNo tasks available.\n")
            return

        for index, task in enumerate(self.task_dict.values(), start=1):
            self.display_task_info(task, index)

        self.report(list(self.task_dict.values()))

    def display_only_done(self) -> None:
        print_menu("Completed Tasks")

        found_task = False

        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] == "Done":
                self.display_task_info(task)
                found_task = True

        if not found_task:
            print("\nNo completed tasks found!\n")

    def display_only_in_process(self) -> None:
        print_menu("Tasks In Process")

        found_task = False

        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] == "In process":
                self.display_task_info(task)
                found_task = True

        if not found_task:
            print("\nNo tasks in process found!\n")

    def display_only_failed(self) -> None:
        print_menu("Failed Tasks")

        found_task = False

        for task in self.task_dict.values(): # Returns all values without keys
            if task["Status"] == "Failed":
                self.display_task_info(task)
                found_task = True

            if not found_task:
                print("\nNo failed tasks found!\n")

    def sort_by_priority_and_display(self) -> None:
        print_menu("Tasks Sorted by Status and Priority")

        done_tasks = []
        in_process_tasks = []
        failed_tasks = []
        other_tasks = []

        for task in self.task_dict.values():
            status = task["Status"]

            if status == "Done":
                done_tasks.append(task)
            elif status == "In process":
                in_process_tasks.append(task)
            elif status == "Failed":
                failed_tasks.append(task)
            else:
                other_tasks.append(task)

        # All variables are list. 
        # Attention: '()' in sorted_tasks are for readability and it is a list, not a tuple.
        # '+' extend the lists together.
        sorted_tasks = (
            self.sort_priority(done_tasks)
            + self.sort_priority(in_process_tasks)
            + self.sort_priority(failed_tasks)
            + self.sort_priority(other_tasks)
        )

        self.task_dict = {
            task["UUID"]: task
            for task in sorted_tasks
        }

        for index, task in enumerate(sorted_tasks, start=1):
            self.display_task_info(task, index)

        self.report(sorted_tasks)

    def sort_priority(self, task_list: list) -> list:
        high_list = []
        medium_list = []
        low_list = []

        for task in task_list:
            if task["Priority"] == "High":
                high_list.append(task)
            elif task["Priority"] == "Medium":
                medium_list.append(task)
            elif task["Priority"] == "Low":
                low_list.append(task)

        return high_list + medium_list + low_list # extend lists into a list 
    
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
            grade_description = "Awfull - what the fuck is this?"

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


    def exit_menu(self, json_file) -> bool:
        print("\n1. Save changes")
        print("2. Discard Changes\n")
        
        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid Value\n")
            return False
        
        if user_select == 1:
            self.save(json_file)
            return True
        
        elif user_select == 2:
            print("Exit 'WITHOUT' saving changes\n")
            return True
    
        print("\nInvalid Value\n")
        return False
