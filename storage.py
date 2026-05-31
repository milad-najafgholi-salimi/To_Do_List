import os
from tkinter import filedialog
import json
# from logic import TaskManager

"""
use graphical inteface for opening and creating. 
Still you need to work with File I/O to read and
write on json file.
"""

def check_selection(user_select):
    if user_select in (1, 2):
        match user_select:
             
            case 1: # Open existing json file
                    
                    selected_file = filedialog.askopenfilename(
                        title="Select an existing file",
                        filetypes=[("JSON files", "*.json")]
                )
                    if selected_file: # selected_path will return True
                        print(f"\nWorking with existing file: {selected_file}\n")
                        #ToDo: need to read and write on the existing file and save changes in this block
                        return selected_file

                        #ToDo: need to connect them via object (self) parameter to the class.
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
                            with open(created_file, "x", encoding="utf-8"):
                                pass
                        except FileExistsError:
                            print(f"\nError: File '{os.path.basename(created_file)}' already exists!\n")
                            return False
                        else:
                             print(f"\nNew file '{os.path.basename(created_file)}' created successfully.\n")
                             return created_file
                        
                    else:   # when you cancel, will return false. So this block will run.
                        print("\nFile creation canceled.\n")
                        return False

    else:
        print("\nInvalid value\n")
        return False


class JsonOperation:
     def read_json_file(json_file : str) -> dict : # Read & take information
        with open(json_file, "r", encoding="utf-8") as file:
          dict_data = json.load(file)
          return dict_data

     def write_json_file(json_file : str) -> str: # write & save - write new json data that has been changed.
         with open(json_file, "w", encoding="utf-8") as file:
          dict_data = json.dump(file)
          return dict_data
