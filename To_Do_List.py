import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        pass
def modify_task():
    modify_task =tasks_listbox.curselection()         # select the task on task add box
    if modify_task:                                                                    # check task is selected or not
        task2 = tasks_listbox.get(modify_task[0])   # assign the selected task to on varible 
        task_entry.insert(tk.END,task2)                       # the selected task is insert into task entry bar
        tasks_listbox.delete(tk.END)                             #then delete the selected task

# == ====== ===== Create the main window ========= ===== ==== = ===== =
root = tk.Tk()
root.title("To Do List")
root.geometry('600x400')

owle_frame = tk.Frame(root, bg='deep sky blue', bd='5', relief='groove')
owle_frame.place(x='60',y='10',width='480',height='380')

titel = tk.Label(root,text='Here you can add your tasks',relief='groove',bg='deep sky blue',bd= 0,fg = 'black',font = ( 'newspaper',14, 'italic'))
titel.place(x='85',y='20',width='300')
# ======== === task entry space ==== ====== ======== ======= = ===
task_entry = tk.Entry(root, width=50,bg='grey',fg='light cyan',bd='4',font=('Arial Black',12, 'bold'))
task_entry.place(x='90',y='65',width='200')

# ======= add button ======== ===  ======
add_button = tk.Button(owle_frame, text="Add Task",bd=4,bg='green',width=10,fg='white' ,command=add_task,font=('Arial Black',8, 'bold'))
add_button.grid(row=0,column=0,pady=10,padx=375)

#=== ========== =  delete button======= ===== ====
delete_button = tk.Button(owle_frame, text="Delete Task",bd=4,bg='red2',width=10,fg='white', command=delete_task,font=('Arial Black',8, 'bold'))
delete_button.grid(row=1,column=0,pady=10,padx=245)

# =============   ==== Modify button ===== ========= ===== ====== =
modify_button = tk.Button(owle_frame, text="Modify Task" ,bd=4,bg='orange2',width=10,fg='gray7',font=('Arial Black',8, 'bold'), command=modify_task)
modify_button.grid(row=2,column=0,pady=10,padx=195)

# Create and pack the tasks listbox
tasks_listbox = tk.Listbox(root, width=50,bd=4,bg='light grey',font=('Arial Black',15, 'bold'))
tasks_listbox.place(x='70',y='180',width='450',height='190')

root.mainloop()
