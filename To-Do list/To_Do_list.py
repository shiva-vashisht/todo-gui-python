import tkinter as tk
from tkinter import messagebox

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [task.strip() for task in file.readlines()]
    except:
        return []

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        tasks.remove(task)
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = load_tasks()

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

# Listbox
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Load tasks into listbox
for task in tasks:
    listbox.insert(tk.END, task)

# Delete button
del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack()

# Run app
root.mainloop()