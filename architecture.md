```mermaid
flowchart LR

    %% =========================
    %% PROGRAM START
    %% =========================

    START([Program Starts]) --> MAIN[main]

    %% =========================
    %% MAIN MENU
    %% =========================

    MAIN --> MAIN_MENU["Display MAIN MENU"]
    MAIN_MENU --> USER_INPUT[/User selects an option/]
    USER_INPUT --> VALID_MAIN_INPUT{"Valid integer?"}

    VALID_MAIN_INPUT -- "No" --> INVALID_MAIN["Print Invalid value"]
    INVALID_MAIN --> MAIN_MENU

    VALID_MAIN_INPUT -- "Yes" --> CHECK_SELECTION["check_selection(user_select)"]

    %% =========================
    %% CHECK SELECTION
    %% =========================

    CHECK_SELECTION --> MAIN_OPTION{"Selected option"}

    MAIN_OPTION -- "1: Open existing file" --> OPEN_FILE["open_existing_file"]
    MAIN_OPTION -- "2: Create new file" --> CREATE_FILE["create_new_file"]
    MAIN_OPTION -- "3: Quit" --> GOODBYE["Print Goodbye"]
    MAIN_OPTION -- "Other" --> INVALID_SELECTION["Print Invalid value"]

    INVALID_SELECTION --> MAIN_END([Program Ends])
    GOODBYE --> MAIN_END

    %% =========================
    %% OPEN EXISTING FILE
    %% =========================

    OPEN_FILE --> FILE_DIALOG_OPEN["Open File Dialog"]
    FILE_DIALOG_OPEN --> FILE_SELECTED{"File selected?"}

    FILE_SELECTED -- "No" --> CANCEL_OPEN["Print File selection cancelled"]
    CANCEL_OPEN --> MAIN_END

    FILE_SELECTED -- "Yes" --> EXISTING_FILE["Return JSON file path"]

    %% =========================
    %% CREATE NEW FILE
    %% =========================

    CREATE_FILE --> FILE_DIALOG_CREATE["Save File Dialog"]
    FILE_DIALOG_CREATE --> PATH_SELECTED{"Path selected?"}

    PATH_SELECTED -- "No" --> CANCEL_CREATE["Print File creation cancelled"]
    CANCEL_CREATE --> MAIN_END

    PATH_SELECTED -- "Yes" --> CREATE_JSON["Create new JSON file"]
    CREATE_JSON --> FILE_EXISTS{"File already exists?"}

    FILE_EXISTS -- "Yes" --> CREATE_ERROR["Print File Exists Error"]
    CREATE_ERROR --> MAIN_END

    FILE_EXISTS -- "No" --> EMPTY_JSON["Write empty list to JSON"]
    EMPTY_JSON --> NEW_FILE["Return new JSON file path"]

    %% =========================
    %% FILE PATH RESULT
    %% =========================

    EXISTING_FILE --> READ_FILE
    NEW_FILE --> READ_FILE

    READ_FILE["read_json_file(json_file)"] --> JSON_READ{"Valid JSON list?"}

    JSON_READ -- "No" --> EMPTY_DATA["Return empty list"]
    JSON_READ -- "Yes" --> DATA["Return task data list"]

    %% =========================
    %% TASK DICTIONARY
    %% =========================

    EMPTY_DATA --> TASK_DICT["Create empty task_dict"]
    DATA --> TASK_DICT

    TASK_DICT --> HAS_DATA{"Data exists?"}

    HAS_DATA -- "Yes" --> LOOP_DATA["Loop through task list"]
    LOOP_DATA --> ADD_DICT["Add task to task_dict using UUID"]
    ADD_DICT --> MORE_TASKS{"More tasks?"}

    MORE_TASKS -- "Yes" --> LOOP_DATA
    MORE_TASKS -- "No" --> CREATE_MANAGER

    HAS_DATA -- "No" --> CREATE_MANAGER["Create TaskManager"]

    %% =========================
    %% TASK MANAGER MENU
    %% =========================

    CREATE_MANAGER --> TASK_MENU["Display TASK MANAGER Menu"]
    TASK_MENU --> TASK_INPUT[/User selects an option/]

    TASK_INPUT --> VALID_TASK_INPUT{"Valid integer?"}

    VALID_TASK_INPUT -- "No" --> TASK_INVALID["Print Invalid value"]
    TASK_INVALID --> TASK_MENU

    VALID_TASK_INPUT -- "Yes" --> TASK_OPTION{"Selected option"}

    %% =========================
    %% TASK ACTIONS
    %% =========================

    TASK_OPTION -- "1: Add task" --> ADD_TASK["manager.add_task"]
    TASK_OPTION -- "2: Remove task" --> REMOVE_TASK["manager.remove_task"]
    TASK_OPTION -- "3: Change status" --> CHANGE_STATUS["manager.change_status"]
    TASK_OPTION -- "4: Change priority" --> CHANGE_PRIORITY["manager.change_priority"]
    TASK_OPTION -- "5: Change description" --> CHANGE_DESCRIPTION["manager.change_description"]
    TASK_OPTION -- "6: Display tasks" --> DISPLAY_MENU
    TASK_OPTION -- "7: Display specific task" --> SHOW_TASK["manager.show_task"]
    TASK_OPTION -- "8: Save" --> SAVE["manager.save(json_file)"]
    TASK_OPTION -- "9: Save and Exit" --> EXIT_MENU
    TASK_OPTION -- "Other" --> TASK_INVALID

    %% =========================
    %% ADD TASK
    %% =========================

    ADD_TASK --> INPUT_TITLE[/Enter title/]
    INPUT_TITLE --> INPUT_DESCRIPTION[/Enter description/]
    INPUT_DESCRIPTION --> GET_PRIORITY["Get priority"]

    GET_PRIORITY --> PRIORITY_INPUT_ADD[/User selects priority/]
    PRIORITY_INPUT_ADD --> VALID_PRIORITY_ADD{"Valid priority?"}

    VALID_PRIORITY_ADD -- "No" --> DEFAULT_LOW_ADD["Set priority to Low"]
    VALID_PRIORITY_ADD -- "Yes" --> SELECTED_PRIORITY_ADD["Return selected priority"]

    DEFAULT_LOW_ADD --> CREATE_TASK
    SELECTED_PRIORITY_ADD --> CREATE_TASK

    CREATE_TASK["Create Task object"] --> GENERATE_UUID["Generate UUID"]
    GENERATE_UUID --> CALCULATE_WEIGHT_NEW["Calculate weight from priority"]
    CALCULATE_WEIGHT_NEW --> TASK_TO_DICT["Convert Task to dictionary"]
    TASK_TO_DICT --> ADD_TO_DICT["Add task to task_dict"]
    ADD_TO_DICT --> TASK_MENU

    %% =========================
    %% SELECT TASK BY UUID
    %% =========================

    REMOVE_TASK --> GET_TASK_UUID
    CHANGE_STATUS --> GET_TASK_UUID
    CHANGE_PRIORITY --> GET_TASK_UUID
    CHANGE_DESCRIPTION --> GET_TASK_UUID
    SHOW_TASK --> GET_TASK_UUID

    GET_TASK_UUID[/Enter UUID/] --> FIND_TASK["Search task_dict by UUID"]
    FIND_TASK --> TASK_FOUND{"Task found?"}

    TASK_FOUND -- "No" --> NOT_FOUND["Print Task not found"]
    NOT_FOUND --> TASK_MENU

    TASK_FOUND -- "Yes" --> SELECTED_TASK["Return selected task"]

    %% =========================
    %% REMOVE TASK
    %% =========================

    SELECTED_TASK --> REMOVE_TASK_DATA["Delete task from task_dict"]
    REMOVE_TASK_DATA --> REMOVE_MESSAGE["Print Task removed"]
    REMOVE_MESSAGE --> TASK_MENU

    %% =========================
    %% CHANGE STATUS
    %% =========================

    SELECTED_TASK --> STATUS_MENU["Display Status Menu"]
    STATUS_MENU --> STATUS_INPUT[/User selects status/]
    STATUS_INPUT --> VALID_STATUS{"Valid status?"}

    VALID_STATUS -- "No" --> DEFAULT_STATUS["Set status to In process"]
    VALID_STATUS -- "Yes" --> SELECTED_STATUS["Return selected status"]

    DEFAULT_STATUS --> UPDATE_STATUS
    SELECTED_STATUS --> UPDATE_STATUS

    UPDATE_STATUS["Update task Status"] --> STATUS_MESSAGE["Print success message"]
    STATUS_MESSAGE --> TASK_MENU

    %% =========================
    %% CHANGE PRIORITY
    %% =========================

    SELECTED_TASK --> PRIORITY_MENU["Display Priority Menu"]
    PRIORITY_MENU --> PRIORITY_INPUT_CHANGE[/User selects priority/]
    PRIORITY_INPUT_CHANGE --> VALID_PRIORITY_CHANGE{"Valid priority?"}

    VALID_PRIORITY_CHANGE -- "No" --> DEFAULT_LOW_CHANGE["Set priority to Low"]
    VALID_PRIORITY_CHANGE -- "Yes" --> SELECTED_PRIORITY_CHANGE["Return selected priority"]

    DEFAULT_LOW_CHANGE --> UPDATE_PRIORITY
    SELECTED_PRIORITY_CHANGE --> UPDATE_PRIORITY

    UPDATE_PRIORITY["Update Priority"] --> UPDATE_WEIGHT["Update Weight"]
    UPDATE_WEIGHT --> PRIORITY_MESSAGE["Print success message"]
    PRIORITY_MESSAGE --> TASK_MENU

    %% =========================
    %% CHANGE DESCRIPTION
    %% =========================

    SELECTED_TASK --> INPUT_NEW_DESCRIPTION[/Enter new description/]
    INPUT_NEW_DESCRIPTION --> UPDATE_DESCRIPTION["Update task Description"]
    UPDATE_DESCRIPTION --> DESCRIPTION_MESSAGE["Print success message"]
    DESCRIPTION_MESSAGE --> TASK_MENU

    %% =========================
    %% SHOW SPECIFIC TASK
    %% =========================

    SELECTED_TASK --> DISPLAY_INFO["Display task information"]
    DISPLAY_INFO --> TASK_MENU

    %% =========================
    %% DISPLAY TASKS MENU
    %% =========================

    DISPLAY_MENU["Display DISPLAY TASKS Menu"]
    DISPLAY_MENU --> DISPLAY_INPUT[/User selects display option/]

    DISPLAY_INPUT --> DISPLAY_OPTION{"Selected option"}

    DISPLAY_OPTION -- "1: All" --> DISPLAY_ALL["display_tasks"]
    DISPLAY_OPTION -- "2: Only Done" --> DISPLAY_DONE["display_only_done"]
    DISPLAY_OPTION -- "3: Only In Process" --> DISPLAY_PROCESS["display_only_in_process"]
    DISPLAY_OPTION -- "4: Only Failed" --> DISPLAY_FAILED["display_only_failed"]
    DISPLAY_OPTION -- "5: Sort by Priority and Status" --> SORT_TASKS["sort_by_priority_and_display"]
    DISPLAY_OPTION -- "Other" --> DISPLAY_INVALID["Print Invalid Value"]

    DISPLAY_INVALID --> TASK_MENU

    %% =========================
    %% DISPLAY ALL TASKS
    %% =========================

    DISPLAY_ALL --> HAS_TASKS{"Any tasks?"}

    HAS_TASKS -- "No" --> NO_TASKS["Print No tasks available"]
    NO_TASKS --> TASK_MENU

    HAS_TASKS -- "Yes" --> LOOP_DISPLAY["Loop through tasks"]
    LOOP_DISPLAY --> DISPLAY_INFO_ALL["Display task information"]
    DISPLAY_INFO_ALL --> MORE_DISPLAY_TASKS{"More tasks?"}

    MORE_DISPLAY_TASKS -- "Yes" --> LOOP_DISPLAY
    MORE_DISPLAY_TASKS -- "No" --> REPORT

    %% =========================
    %% FILTER TASKS
    %% =========================

    DISPLAY_DONE --> FILTER_DONE["Find tasks with Status equal to Done"]
    DISPLAY_PROCESS --> FILTER_PROCESS["Find tasks with Status equal to In process"]
    DISPLAY_FAILED --> FILTER_FAILED["Find tasks with Status equal to Failed"]

    FILTER_DONE --> DISPLAY_FILTERED
    FILTER_PROCESS --> DISPLAY_FILTERED
    FILTER_FAILED --> DISPLAY_FILTERED

    DISPLAY_FILTERED["Display filtered tasks"] --> FOUND_FILTERED{"Any matching tasks?"}

    FOUND_FILTERED -- "Yes" --> DISPLAY_MATCHING["Display matching tasks"]
    FOUND_FILTERED -- "No" --> NO_MATCH["Print No matching tasks found"]

    DISPLAY_MATCHING --> TASK_MENU
    NO_MATCH --> TASK_MENU

    %% =========================
    %% SORT TASKS
    %% =========================

    SORT_TASKS --> SPLIT_STATUS["Separate tasks by status"]

    SPLIT_STATUS --> DONE_LIST["Done tasks"]
    SPLIT_STATUS --> PROCESS_LIST["In Process tasks"]
    SPLIT_STATUS --> FAILED_LIST["Failed tasks"]
    SPLIT_STATUS --> OTHER_LIST["Other tasks"]

    DONE_LIST --> SORT_PRIORITY_DONE["Sort Done tasks by priority"]
    PROCESS_LIST --> SORT_PRIORITY_PROCESS["Sort In Process tasks by priority"]
    FAILED_LIST --> SORT_PRIORITY_FAILED["Sort Failed tasks by priority"]
    OTHER_LIST --> SORT_PRIORITY_OTHER["Sort Other tasks by priority"]

    SORT_PRIORITY_DONE --> COMBINE_LISTS
    SORT_PRIORITY_PROCESS --> COMBINE_LISTS
    SORT_PRIORITY_FAILED --> COMBINE_LISTS
    SORT_PRIORITY_OTHER --> COMBINE_LISTS

    COMBINE_LISTS["Combine sorted lists"] --> UPDATE_TASK_DICT_SORTED["Rebuild task_dict"]

    UPDATE_TASK_DICT_SORTED --> DISPLAY_SORTED["Display sorted tasks"]
    DISPLAY_SORTED --> REPORT

    %% =========================
    %% REPORT
    %% =========================

    REPORT["Generate report"] --> REPORT_EMPTY{"Data exists?"}

    REPORT_EMPTY -- "No" --> NOTHING_CALCULATE["Print Nothing to calculate"]
    NOTHING_CALCULATE --> TASK_MENU

    REPORT_EMPTY -- "Yes" --> COUNT_TASKS["Count total tasks"]
    COUNT_TASKS --> COUNT_STATUS["Count Done, Failed, and In Process tasks"]
    COUNT_STATUS --> CALCULATE_TOTAL_WEIGHT["Calculate total weight"]
    CALCULATE_TOTAL_WEIGHT --> CALCULATE_DONE_WEIGHT["Calculate weight of Done tasks"]
    CALCULATE_DONE_WEIGHT --> CALCULATE_PERCENTAGES["Calculate percentages"]
    CALCULATE_PERCENTAGES --> CALCULATE_GRADE["Calculate grade"]
    CALCULATE_GRADE --> DISPLAY_REPORT["Display report"]
    DISPLAY_REPORT --> TASK_MENU

    %% =========================
    %% SAVE
    %% =========================

    SAVE --> PREPARE_TASK_LIST["Convert task_dict values to list"]
    PREPARE_TASK_LIST --> REBUILD_DICT_SAVE["Rebuild task_dict"]
    REBUILD_DICT_SAVE --> WRITE_TASK_FILE["write_json_file"]
    WRITE_TASK_FILE --> SAVE_TASKS["Save tasks to JSON"]

    SAVE_TASKS --> GENERATE_REPORT["Generate report"]
    GENERATE_REPORT --> REPORT_FILE["Create report filename"]
    REPORT_FILE --> WRITE_REPORT_FILE["write_json_file"]
    WRITE_REPORT_FILE --> SAVE_REPORT["Save report JSON"]
    SAVE_REPORT --> TASK_MENU

    %% =========================
    %% EXIT MENU
    %% =========================

    EXIT_MENU["Display Exit Menu"]
    EXIT_MENU --> EXIT_INPUT[/User selects/]

    EXIT_INPUT --> EXIT_OPTION{"Selected option"}

    EXIT_OPTION -- "1: Save changes" --> SAVE_EXIT["Save changes"]
    SAVE_EXIT --> END_TASK_MANAGER["Exit Task Manager"]

    EXIT_OPTION -- "2: Discard changes" --> DISCARD["Discard changes"]
    DISCARD --> END_TASK_MANAGER

    EXIT_OPTION -- "Other" --> EXIT_INVALID["Print Invalid Value"]
    EXIT_INVALID --> TASK_MENU

    END_TASK_MANAGER --> MAIN_MENU
