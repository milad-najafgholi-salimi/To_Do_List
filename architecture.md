```mermaid
flowchart LR
    Start([Start]) --> MainMenu{Main Menu}
    
    MainMenu --> |User selects 1| OpenFile[Open existing file via dialog]
    MainMenu --> |User selects 2| CreateFile[Create new file via dialog]
    MainMenu --> |User selects 3| Quit([Quit Program])
    
    OpenFile --> CheckFile1{File selected?}
    CreateFile --> CheckFile2{File created?}
    
    CheckFile1 --> |No| MainMenu
    CheckFile1 --> |Yes| ReadJSON[Read JSON file]
    
    CheckFile2 --> |No| MainMenu
    CheckFile2 --> |Yes| ReadJSON
    
    ReadJSON --> LoadData[Load existing tasks into task_list]
    LoadData --> TaskManagerMenu
    
    TaskManagerMenu[Task Manager Menu] --> TMMenu{User Choice}
    
    TMMenu --> |1| AddTask[Add Task]
    TMMenu --> |2| RemoveTask[Remove Task]
    TMMenu --> |3| ChangeStatus[Change Status]
    TMMenu --> |4| DisplayAll[Display All Tasks]
    TMMenu --> |5| DisplaySpecific[Display Specific Task]
    TMMenu --> |6| Save[Save to JSON]
    TMMenu --> |7| Exit[Exit & Auto-save]
    
    AddTask --> AddStep1[Generate UUID]
    AddStep1 --> AddStep2[Input Title]
    AddStep2 --> AddStep3[Input Description]
    AddStep3 --> AddStep4[Set Priority]
    AddStep4 --> AddStep5[Convert to dict]
    AddStep5 --> AddStep6[Append to task_list]
    AddStep6 --> TaskManagerMenu
    
    RemoveTask --> RemoveStep1[Enter UUID]
    RemoveStep1 --> RemoveStep2{UUID found?}
    RemoveStep2 --> |Yes| RemoveStep3[Remove task from list]
    RemoveStep2 --> |No| RemoveError[Show Not Found]
    RemoveStep3 --> TaskManagerMenu
    RemoveError --> TaskManagerMenu
    
    ChangeStatus --> StatusStep1[Enter UUID]
    StatusStep1 --> StatusStep2{UUID found?}
    StatusStep2 --> |Yes| StatusStep3[Set Status to 'Done']
    StatusStep2 --> |No| StatusError[Show Not Found]
    StatusStep3 --> TaskManagerMenu
    StatusError --> TaskManagerMenu
    
    DisplayAll --> DisplayStep1{task_list empty?}
    DisplayStep1 --> |Yes| DisplayEmpty[Show 'No tasks available']
    DisplayStep1 --> |No| DisplayLoop[Loop through and print each task]
   