import json
import os
from datetime import datetime
from typing import List, Dict, Any
 
class Task:
    """Represents a single task""" 
     
    def __init__(self, task_id: int, description: str, status: str = "pending"):
        self.id = task_id
        self.description = description
        self.status = status  # "pending" or "completed"
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_date": self.created_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary"""
        task = cls(data["id"], data["description"], data["status"])
        task.created_date = data["created_date"]
        return task

class TaskManager:
    """Main task manager class"""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, description: str) -> None:
        """Add a new task"""
        if not description.strip():
            print("Error: Task description cannot be empty!")
            return
        
        task = Task(self.next_id, description.strip())
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task '{description}' added successfully!")
    
    def view_tasks(self) -> None:
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n" + "="*50)
        print("YOUR TASKS")
        print("="*50)
        
        for task in self.tasks:
            status_symbol = "✓" if task.status == "completed" else "○"
            print(f"{status_symbol} [{task.id}] {task.description}")
            print(f"    Created: {task.created_date}")
            print(f"    Status: {task.status.upper()}")
            print("-" * 30)
    
    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed"""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found!")
            return
        
        if task.status == "completed":
            print(f"Task '{task.description}' is already completed!")
            return
        
        task.status = "completed"
        self.save_tasks()
        print(f"Task '{task.description}' marked as completed!")
    
    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID"""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found!")
            return
        
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task '{task.description}' deleted successfully!")
    
    
    
def display_menu():
    """Display the main menu"""
    print("\n" + "="*30)
    print("PERSONAL TASK MANAGER")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-"*30)

def get_user_choice() -> int:
    """Get and validate user menu choice"""
    try:
        choice = int(input("Enter your choice (1-5): "))
        if 1 <= choice <= 5:
            return choice
        else:
            print("Please enter a number between 1 and 5.")
            return 0
    except ValueError:
        print("Please enter a valid number.")
        return 0

def main():
    """Main program loop"""
    task_manager = TaskManager()
    
    print("Welcome to Personal Task Manager!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:  # Add Task
            description = input("Enter task description: ")
            task_manager.add_task(description)
        
        elif choice == 2:  # View Tasks
            task_manager.view_tasks()
        
        elif choice == 3:  # Complete Task
            try:
                task_id = int(input("Enter task ID to complete: "))
                task_manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID number.")
        
        elif choice == 4:  # Delete Task
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID number.")
        
        elif choice == 5:  # Exit
            print("Thank you for using Personal Task Manager!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":

    main()



