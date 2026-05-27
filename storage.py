import os
from tkinter import filedialog

"""
use graphical inteface for opening and creating. 
Still you need to work with File I/O to read and
write on json file.
"""

def check_selection(usr_select):
    if usr_select in (1, 2):
        match usr_select:
            case 1: # Open existing json file:
                    selected_path = filedialog.askopenfilename(
                        title="Select an existing file",
            filetypes=[("JSON files", "*.json")]
                )
                    if selected_path: # selected_path will return True
                        print(f"\nWorking with existing file: {selected_path}\n")
                        #ToDo: need to read and write on the existing file and save changes in this block
                        #ToDo: need to connect them via object (self) parameter to the class.
                    else:  # when you cancel, will return false. So this block will run.
                        print("\nFile selection cancelled!\n")
                        return False

            case 2: # create new json file
                    
                    selected_path = filedialog.asksaveasfilename(
                        title="Specify path and name for the new file",
                        defaultextension=".json", # Default extension if user doesn't provide one
                        filetypes=[("JSON files", "*.json")]
                    )
                    if selected_path: # selected_path will return True
                        try:
                            with open(selected_path, "x", encoding="utf-8"):
                                print(f"\nNew file '{os.path.basename(selected_path)}' created successfully.\n")
                        except FileExistsError:
                            print(f"\nError: File '{os.path.basename(selected_path)}' already exists!\n")
                            return False
                    else:   # when you cancel, will return false. So this block will run.
                        print("\nFile creation canceled.\n")
                        return False

    else:
        print("Invalid value")
        return False


print("\n--File--\n")
print("1. Open existing file\n 2. Create new file\n")

try:
    usr_select = int(input("Select: "))
    check_selection(usr_select)
except ValueError:
    print("\nInvalid value\n")