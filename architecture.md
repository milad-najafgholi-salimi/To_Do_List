```mermaid

flowchart LR
    A([Start]) --> B[/Import modules/]
    B --> C{While True<br>Main Menu}
    
    C --> D[/Display Main Menu/]
    D --> E[/Get user_select/]
    E --> F{Valid integer?}
    F -->|No| G[/Print Invalid value/]
    G --> Z([End])
    
    F -->|Yes| H{user_select?}
    
    H -->|1 or 2| I[check_selection]
    H -->|3| J[/Print Goodbye/]
    J --> Z
    
    I --> K{user_select == 1?}
    K -->|Yes - Open file| L[/filedialog.askopenfilename/]
    K -->|No - Create file| M[/filedialog.asksaveasfilename/]
    
    L --> N{File selected?}
    N -->|No| O[/Print Cancelled/]
    O --> Z
    N -->|Yes| P[Return file path]
    
    M --> Q{File created?}
    Q -->|No| R[/Print Cancelled/]
    R --> Z
    Q -->|Yes| S[Create empty JSON file]
    S --> T[Return file path]
    
    P --> U[json_file = file path]
    T --> U
    
    U --> V{json_file and user_select==1?}
    V -->|No| Z
    V -->|Yes| W{While True<br>Task Menu}
    
    W --> X[/Display Task Menu/]
    X --> Y[read_json_file]
    Y --> AA[task_list.extend]
    AA --> AB[user_choice]
    
    AB --> AC{Valid integer<br>1-7?}
    AC -->|No| AD[/Print Invalid/]
    AD --> W
    
    AC -->|Yes| AE{match user_select}
    
    AE -->|1| AF[add_task]
    AE -->|2| AG[remove_task]
    AE -->|3| AH[change_status]
    AE -->|4| AI[display]
    AE -->|5| AJ[show_task]
    AE -->|6| AK[save]
    AE -->|7| AL[exit]
    
    AF --> AM[Get title & description]
    AM --> AN[Create Task object]
    AN --> AO[Generate UUID]
    AO --> AP[Set priority]
    AP --> AQ[Create task dict]
    AQ --> AR[Append to task_list]
    AR --> W
    
    AG --> AS[task_uuid]
    AS --> AT{Found?}
    AT -->|Yes| AU[Remove from task_list]
    AU --> W
    AT -->|No| AV[Print Not found]
    AV --> W
    
    AH --> AW[task_uuid]
    AW --> AX{Found?}
    AX -->|Yes| AY[Set Status to Done]
    AY --> W
    AX -->|No| AZ[Print Not found]
    AZ --> W
    
    AI --> BA[Print all tasks]
    BA --> W
    
    AJ --> BB[task_uuid]
    BB --> BC{Found?}
    BC -->|Yes| BD[Print specific task]
    BD --> W
    BC -->|No| BE[Print Not found]
    BE --> W
    
    AK --> BF[write_json_file]
    BF --> BG[Save to file]
    BG --> W
    
    AL --> BH[Return False]
    BH --> Z
    
    Z([End])
