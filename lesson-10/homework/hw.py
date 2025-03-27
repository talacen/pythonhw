######### 1.1 # defining task class

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} - {self.status} (Due: {self.due_date})"

######### 1.2 # defining todo list class

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_tasks(self):
        return "\n".join(str(task) for task in self.tasks)

    def list_incomplete_tasks(self):
        return "\n".join(str(task) for task in self.tasks if task.status == "Incomplete")

######### 1.3 # main program 

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(Task(title, description, due_date))
            print("Task added successfully!")
        elif choice == "2":
            title = input("Enter task title to mark as complete: ")
            if todo_list.mark_task_complete(title):
                print("Task marked as complete!")
            else:
                print("Task not found!")
        elif choice == "3":
            print("\nAll Tasks:")
            print(todo_list.list_tasks())
        elif choice == "4":
            print("\nIncomplete Tasks:")
            print(todo_list.list_incomplete_tasks())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

######### 1.4 #test

if __name__ == "__main__":
    main()
