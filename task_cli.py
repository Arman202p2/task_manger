import sys
import os
import json
from datetime import datetime
tasks_file = "tasks.json"
def main():
    if len(sys.argv)<2:
        print("Usage: python tasks_cli.py <command> [agrs]")
        return
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv)<3:
            print("Error: Missing task description")
        else:
            add_task(sys.argv[2])
    elif command == "list":
        if len(sys.argv)==3:
            list_find(sys.argv[2])
        else:
            list_tasks()
    elif command == "update":
        if len(sys.argv)<4:
            print("Error: Missing task description")
        else:
            update_task(int(sys.argv[2]),sys.argv[3])
    elif command == "mark-in-progress":
        if len(sys.argv)<3:
            print("Error: Missing task description")
        else:
            mark_status(int(sys.argv[2]),'in-progress')
    elif command == "mark-done":
        if len(sys.argv)<3:
            print("Error: Missing task description")
        else:
            mark_status(int(sys.argv[2]),'done')
    elif command == "delete":
        if len(sys.argv)<3:
            print("Error: Missing task description")
        else:
            delete_task(int(sys.argv[2]))
    else:
        print(f"Unknown command: {command}")

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    try:
        with open(tasks_file,'r') as file:
            return json.load(file)
    except:
        return []
def save_tasks(tasks):
    try:
        with open(tasks_file,'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error in saving tasks:{e}")
def add_task(desc):
    tasks = load_tasks()
    if not tasks:
        new_id = 1
    else:
        new_id = max(t["id"] for t in tasks) + 1
    new_task = {
        "id": new_id,
        "description": desc,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks():
    tasks= load_tasks()
    if not tasks:
        print("No Task Found")
        return
    print(f"{'ID':<5}{'Status':<12}{'Description'}")
    print("-"*40)
    for task in tasks:
        print(f"{task['id']:<5}{task['status']:<12}{task['description']}")
def delete_task(del_task_id):
    
    tasks = load_tasks()
    initial_count=len(tasks)
    tasks = [task for task in tasks if task['id']!=int(del_task_id)]
    if initial_count == len(tasks):
        print(f"Task{del_task_id} not found")
    else:
        save_tasks(tasks)
        print(f"Task{del_task_id} deleted")

def update_task(task_id,new_desc):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task['id']==task_id:
            task['description']=new_desc
            task['updatedAt']=datetime.now().isoformat()
            found = True
            save_tasks(tasks)
            print(f"{task['id']} is updated")
            return
    if not found:  
        print(f"{task_id} does not exist")
def list_find(find):
    tasks = load_tasks()
    
    print(f"{'ID':<5}{'Status':<12}{'Description'}")
    print("-"*40)
    for task in tasks:
        if task['status']==find:
            
            print(f"{task['id']:<5}{task['status']:<12}{task['description']}")

def mark_status(task_id,new_status):
    
    tasks = load_tasks()
    for task in tasks:
        if task['id']==task_id:
            task['status']=new_status
            save_tasks(tasks)
            print(f"{task['id']} status updated to {task['status']}")
            return
    print(f"{task_id} does not exist")
    return
            

    

if __name__=="__main__":
    main()