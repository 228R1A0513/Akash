import sqlite3

# Initialize SQLite database connection
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              description TEXT,
              status TEXT DEFAULT 'Pending')''')
conn.commit()

def add_task(title, description=''):
    c.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    print("Task added successfully!")

def mark_complete(task_id):
    try:
        c.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
        conn.commit()
        print("Task marked as completed!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Status: {task[3]}")
    else:
        print("No tasks found.")

def delete_task(task_id):
    try:
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        print("Task deleted successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                mark_complete(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    conn.close()
