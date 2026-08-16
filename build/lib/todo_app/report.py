def generate_report(data: list) -> dict: 
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

    report_data = {
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
    
    return report_data

def display_report(report_data):
    print("\n" + "="*50)
    print("Task Completion Report")
    print("="*50)

    for key, value in report_data.items():
        print(f"{key}: {value}")

    print("="*50 + "\n")