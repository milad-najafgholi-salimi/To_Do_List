# ToDo List CLI Application

A command-line task management application built with Python. It provides a structured way to create, manage, organize, and track tasks through a simple CLI interface.

The application supports priority levels, status tracking, UUID-based task selection, sorting, progress reports, weighted completion scoring, and persistent JSON storage.

## Features

* **Add tasks** — create tasks with a title, description, priority, and status.

* **Modify tasks** — change a task's description, priority, or status.

* **Delete tasks** — remove tasks by selecting their UUID.

* **View tasks** — display all tasks or view a specific task using its UUID.

* **Priority levels** — assign one of three priority levels: `Extremelly Important`, `High`, `Medium`, or `Low`.

* **Weighted priority system** — each priority level has a different weight:

  * `Extremelly Important` → 4
  * `High` → 3
  * `Medium` → 2
  * `Low` → 1

* **Status tracking** — tasks can have one of the following statuses:

  * `Done`
  * `In process`
  * `Failed`

* **Filter tasks by status** — view only completed, in-process, or failed tasks.

* **Sort tasks** — organize tasks first by status and then by priority.

* **Task reports** — generate statistics including:

  * Total number of tasks
  * Total task weight
  * Completed tasks
  * Failed tasks
  * In-process tasks
  * Completion percentages
  * Weighted completion percentage
  * Overall grade from `A` to `F`

* **Weighted progress grading** — task completion is evaluated based on task weights, so completing a high-priority task has a greater impact on the overall progress score than completing a low-priority task.

* **UUID-based task selection** — every task receives a unique UUID, making it easy to find and manage a specific task.

> **Tip:** To modify or manage a specific task, display the tasks, copy the task's UUID, and paste it when the application asks you to enter a UUID.

* **JSON persistence** — all tasks are stored in simple, readable JSON files.

* **Separate report files** — saving tasks also generates a separate JSON report file containing task statistics.

* **File dialog support** — use a graphical file dialog to open an existing JSON file or create a new one without manually typing file paths.

* **Reusable menu system** — menu headers and option lists are generated through a reusable `print_menu()` utility.

* **Reusable task display logic** — task information is displayed through a centralized `display_task_info()` method, reducing duplicated code.

## Installation

### Prerequisites

* Python 3.12 or higher
* pip 21 or higher

The project was developed and tested with Python 3.12. Using Python 3.12 or a newer version is recommended.

The application may also work with older Python versions, but compatibility with older versions is not guaranteed.

### Installation Methods

#### Method 1: Editable Install — Recommended for Development

This method installs the package in development mode. Changes made to the source code will be immediately reflected when running the application.

```bash
git clone https://github.com/milad-najafgholi-salimi/To_Do_List.git

cd To_Do_List

pip install -e .
```

#### Method 2: Install Directly from GitHub

You can install the project directly without manually cloning the repository:

```bash
pip install git+https://github.com/milad-najafgholi-salimi/To_Do_List.git
```

#### Method 3: Standard Install

```bash
git clone https://github.com/milad-najafgholi-salimi/To_Do_List.git

cd To_Do_List

pip install .
```

## Quick Start

After installation, run the application with:

```bash
todo-app
```

The application will guide you through the available options for opening an existing task file, creating a new task file, or exiting the program.

## Why This Project?

I built this project to solve an actual need I had while improving my programming skills.

The idea started as a set of text-based requirements generated with the help of AI. I then designed and implemented the application myself, gradually improving its structure through refactoring and practice.

I did use AI as a learning and development tool for explanations, debugging assistance, and guidance. However, I did not simply copy the main code from AI.

Working on this project helped me:

* Become more comfortable with Object-Oriented Programming (OOP), which I had previously struggled with.

* Practice reading from and writing to JSON files.

* Improve my understanding of modular programming.

* Practice separating application logic, storage operations, and user interface utilities.

* Handle user input and invalid input more carefully.

* Practice working with dictionaries, lists, and list transformations.

* Build a complete CLI application from scratch.

* Improve code readability and reduce duplicated code through refactoring.

## 🤝 Contributing

I welcome contributions, suggestions, and bug reports.

This is an evolving project, and I plan to continue improving it with new features and enhancements.

Feel free to:

* Report bugs
* Suggest new features
* Submit pull requests
* Share feedback
* Suggest improvements to the code structure

## 📄 License

This project is open-source and free to use.

You are welcome to modify, distribute, and use the code in your own projects according to the terms of the project's license.

## 👤 Author

**Milad Najafgholi Salimi**

* GitHub: `@milad-najafgholi-salimi`

Built with ❤️ for learning and productivity.
