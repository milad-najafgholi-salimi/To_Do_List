from .ui import print_menu, wait_for_user, display_task_info
from .task import Task
from .report import generate_report, display_report

class TaskManager:
    def __init__(self, task_dict):
        self.task_dict = task_dict

    def get_all_tasks(self) -> list[dict]:
        return list(self.task_dict.values())

    def get_tasks_by_status(self, status: str) -> list[dict]:
        return [
            task
            for task in self.task_dict.values()
            if task["Status"] == status
        ]

    def add_task(self, title: str, description: str, priority: str) -> None:
        task = Task(title=title, description=description, priority=priority)

        self.task_dict[task.uuid] = task.to_dict()

    def remove_task(self, uuid: str) -> bool:
        task = self.task_dict.get(uuid)

        if task is None:
            return False

        del self.task_dict[uuid]
        return True

    def change_status(self, uuid: str, status: str) -> bool:
        task = self.task_dict.get(uuid)

        if task is None:
            return False

        task["Status"] = status
        return True

    def change_priority(self, uuid: str, priority: str) -> bool:
        task = self.task_dict.get(uuid)

        if task is None:
            return False

        task["Priority"] = priority
        task["Weight"] = Task.PRIORITY_WEIGHTS.get(priority, 1)

        return True

    def change_description(self, uuid: str, description: str) -> bool:
        task = self.task_dict.get(uuid)

        if task is None:
            return False

        task["Description"] = description

        return True
    
    def show_task(self):
        print_menu("Displaying a Specific Task")

        uuid = input("\nEnter UUID: ")

        task = self.task_dict.get(uuid)

        if task is None:
            print("\nTask not found!\n")
            return

        display_task_info(task)

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
            display_task_info(task, index)

        report_data = generate_report(sorted_tasks)
        display_report(report_data)

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
    
    def exit_menu(self, json_file) -> bool:
        from .save import save
        print("\n1. Save changes")
        print("2. Discard Changes\n")
        
        try:
            user_select = int(input("Select: "))
        except ValueError:
            print("\nInvalid Value\n")
            wait_for_user()
            return False
        
        if user_select == 1:
            self.task_dict = save(self.task_dict, json_file)
            wait_for_user()
            return True
        
        elif user_select == 2:
            print("Exit 'WITHOUT' saving changes\n")
            wait_for_user()
            return True
    
        print("\nInvalid Value\n")
        wait_for_user()
        return False
