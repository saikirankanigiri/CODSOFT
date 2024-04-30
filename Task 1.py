import tkinter as tk
from tkinter import messagebox

user_tasks = []

def display_user_tasks():
    if not user_tasks:
        messagebox.showinfo("To-Do List", "Your to-do list is empty.")
    else:
        task_list = "\n".join([f"{i}. {task['name']} ({'Done' if task['completed'] else 'Not Done'})" for i, task in enumerate(user_tasks, start=1)])
        messagebox.showinfo("To-Do List", f"To-Do List:\n{task_list}")

def add_user_task():
    task_name = user_task_entry.get()
    if task_name:
        task = {"name": task_name, "completed": False}
        user_tasks.append(task)
        messagebox.showinfo("To-Do List", f"Task '{task_name}' added to your to-do list.")
        user_task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("To-Do List", "Please enter a task.")

def mark_task_completed():
    task_number = task_number_entry.get()
    if task_number.isdigit():
        task_number = int(task_number)
        if 1 <= task_number <= len(user_tasks):
            user_tasks[task_number - 1]["completed"] = True
            messagebox.showinfo("To-Do List", f"Task {task_number} marked as completed.")
            task_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("To-Do List", "Invalid task number. Please enter a valid task number.")
    else:
        messagebox.showerror("To-Do List", "Invalid task number. Please enter a valid task number.")

def remove_user_task():
    task_number = task_number_entry.get()
    if task_number.isdigit():
        task_number = int(task_number)
        if 1 <= task_number <= len(user_tasks):
            removed_task = user_tasks.pop(task_number - 1)
            messagebox.showinfo("To-Do List", f"Task '{removed_task['name']}' removed from your to-do list.")
            task_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("To-Do List", "Invalid task number. Please enter a valid task number.")
    else:
        messagebox.showerror("To-Do List", "Invalid task number. Please enter a valid task number.")

root = tk.Tk()
root.title("To-Do List App")

# Task entry
task_label = tk.Label(root, text="Task:")
task_label.grid(row=0, column=0, padx=10, pady=5)
user_task_entry = tk.Entry(root, width=30)
user_task_entry.grid(row=0, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_user_task)
add_button.grid(row=0, column=2, padx=10, pady=5)

display_button = tk.Button(root, text="Display Tasks", command=display_user_tasks)
display_button.grid(row=1, column=0, padx=10, pady=5)

mark_button = tk.Button(root, text="Mark Completed", command=mark_task_completed)
mark_button.grid(row=1, column=1, padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_user_task)
remove_button.grid(row=1, column=2, padx=10, pady=5)

# Task number entry
task_number_label = tk.Label(root, text="Task Number:")
task_number_label.grid(row=2, column=0, padx=10, pady=5)
task_number_entry = tk.Entry(root, width=10)
task_number_entry.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
