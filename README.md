# ToDo List CLI Application
A command-line task management tool built with Python. It includes features like priority levels, status tracking, sorting, and report generation with weighted grading. All tasks are stored persistently in JSON files.

## Features
- Add, edit, delete, and view tasks — everything you need for basic task management

- Priority levels — High, Medium, or Low, with **weighted scoring** for better progress tracking

- Status tracking — mark tasks as Done, In process, Failed, or use your own custom status

- Filter and sort — view tasks by status, or sort them by priority and status together

- Task reports — see completion stats, weighted scores, and get a grade (A to F) based on progress

- Save to JSON — all tasks are stored in simple, readable JSON files

- Separate report files — each save creates a report file alongside your task file

- UUID for each task — makes it easy to find and manage specific tasks

#### **(Hint: Display tasks and just copy UUID task via `ctrl+Lshift+c` then paste it via `ctrl+Lshift+v` to modify task)**

- File dialog — use a simple GUI window to open or create task files (no need to type file paths)

## Installation

### Prerequisites
- Python 3.12 or higher
- pip (version 21+)

This has been developed on this specific version (Python 3.12) of Python, and using that version is recommended, but it is also compatible with newer versions. It may also work well with older versions.

### Installation Methods

#### **Method 1: Editable Install (Recommended for Development)**

This method installs the package in development mode, meaning any changes you make to the code will take effect immediately.

```
git clone https://github.com/milad-najafgholi-salimi/To_Do_List.git
```
```
cd To_Do_List
```
```
pip install -e .
```
#### **Method 2: Install Directly from GitHub**
No need to clone the repository manually — pip will handle everything.
```
pip install git+https://github.com/milad-najafgholi-salimi/To_Do_List.git
```
#### **Method 3: Standard Install (After Cloning)**
```
git clone https://github.com/milad-najafgholi-salimi/To_Do_List.git
```
```
cd To_Do_List
```
```
pip install .
```

## Quick Start
After installation, run the application with:
```
todo-app
```

## Why This Project?
I built this project to solve an actual need I had, and to get better at programming in the process. The idea started as a set of text-based requirements from an AI — I then implemented the whole thing myself, without looking at any pre-written code.

(**But I did use AI as a tool to get help — nevertheless, not to directly take the main code.**)

Working on this helped me:
- Get more comfortable with OOP (which I had struggled with before)

- Practice reading from and writing to JSON files

- Handle user input and errors more carefully

- Build a complete CLI tool from scratch

## Key Technical Features
- Weighted Priority System: Tasks have different weights based on priority for more accurate progress tracking

- UUID Generation: Ensures unique identification for each task

- JSON Persistence: All data stored in human-readable JSON format

- Report Generation: Creates separate report files for analytics

- Graceful Error Handling: User-friendly error messages and validation

## 🤝 Contributing
I welcome contributions, suggestions, and bug reports! This is an evolving project, and I plan to continue improving it with new features and enhancements. Feel free to:

- Report issues

- Suggest new features

- Submit pull requests

- Share your feedback

## 📄 License
This project is open-source and completely free to use. Feel free to modify, distribute, or use it in your own projects.

## 👤 Author
Milad Najafgholi Salimi

- GitHub: @milad-najafgholi-salimi

Built with ❤️ for learning and productivity