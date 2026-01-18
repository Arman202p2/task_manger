# Task Tracker CLI

This is a solution to the **[Task Tracker](https://roadmap.sh/projects/task-tracker)** challenge on roadmap.sh.

## Project URL
https://roadmap.sh/projects/task-tracker

## Features
- Add, Update, and Delete tasks
- Mark tasks as In-Progress or Done
- List all tasks or filter by status (`done`, `todo`, `in-progress`)
- Data persists in a local JSON file

## How to Run
1. Clone the repository
2. Run commands:
   ```bash
   python tasks_cli.py add "Buy milk"
   python tasks_cli.py list
   python tasks_cli.py mark-done 1