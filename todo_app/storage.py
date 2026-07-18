import json
from pathlib import Path
from tkinter import filedialog

def open_existing_file() -> str | bool: # return file path or False
    selected_file = filedialog.askopenfilename(
        title="Select an existing file",
        filetypes=[("JSON files", "*.json")]
    )

    if selected_file:
        print(f"\nWorking with existing file: {selected_file}\n")
        return selected_file

    print("\nFile selection cancelled!\n")
    return False

def create_new_file() -> str | bool: # return file path or False
    file_path = filedialog.asksaveasfilename(
        title="Specify path and name for the new file",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )

    if not file_path:
        print("\nFile creation cancelled.\n")
        return False

    try:
        with open(file_path, "x", encoding="utf-8") as file:
            json.dump([], file, indent=4)

    except FileExistsError:
        print(
            f"\nError: File '{Path(file_path).name}' "
            "already exists!\n"
        )
        return False

    print(
        f"\nNew file '{Path(file_path).name}' "
        "created successfully.\n"
    )

    return file_path

def check_selection(user_select: int) -> str | bool:
    match user_select:

        case 1:
            return open_existing_file()

        case 2:
            return create_new_file()

        case 3:
            print("\n--Goodbye--\n")
            return False

        case _:
            print("\nInvalid value\n")
            return False

def read_json_file(json_file: str) -> list:
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []

    except (json.JSONDecodeError, FileNotFoundError):
        return []

# write & save - write new json data that has been change.
def write_json_file(json_file: str, data: list) -> None:
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
