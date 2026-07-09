import os
from tkinter import filedialog
import json

"""
use graphical inteface for opening and creating. 
Still you need to work with File I/O to read and
write on json file.
"""

def check_selection(user_select):
    if user_select in (1, 2, 3):
        match user_select:
             
            case 1: # Open existing json file
                    
                    selected_file = filedialog.askopenfilename(
                        title="Select an existing file",
                        filetypes=[("JSON files", "*.json")]
                )
                    if selected_file: # selected_path will return True
                        print(f"\nWorking with existing file: {selected_file}\n")
                        return selected_file

                    else:  # when you cancel, will return false. So this block will run.
                        print("\nFile selection cancelled!\n")
                        return False

            case 2: # create new json file
                    
                    created_file = filedialog.asksaveasfilename(
                        title="Specify path and name for the new file",
                        defaultextension=".json", # Default extension if user doesn't provide one
                        filetypes=[("JSON files", "*.json")]
                    )
                    if created_file: # created_file will return True
                        try:
                            with open(created_file, "x", encoding="utf-8") as file:
                                json.dump([], file, indent=4)
                        except FileExistsError:
                            print(f"\nError: File '{os.path.basename(created_file)}' already exists!\n")
                            return False
                        else:
                             print(f"\nNew file '{os.path.basename(created_file)}' created successfully.\n")
                             return created_file
                        
                    else:   # when you cancel, will return false. So this block will run.
                        print("\nFile creation canceled.\n")
                        return False
            
            case 3: # Quit and close program completely
                print("\n--Goodbye--\n")
                return False

    else:
        print("\nInvalid value\n")
        return False


def read_json_file(json_file : str) : # Read & take information
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            if os.path.getsize(json_file) == 0:
                return []
            data = json.load(file) # data is a list with dictionary elements, if it wasn't empty.
            return data if isinstance(data, list) else [] # Checks the content are correct or not;
    except (json.JSONDecodeError, FileNotFoundError):                                        # and returns an empty list if it wasn't.
        return []

def write_json_file(json_file : str, data_as_list : list) -> str:
    """
    write & save - write new json data that has been change.
    """
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data_as_list, file, indent=4)
