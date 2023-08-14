import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.title("To_Do_List")
def add_task():
    task = entry_task.get()
    if task!="" :
        Listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="you must enter a task.")
def delete_task():
    try:
        task_index=Listbox_tasks.curselection()[0]
        Listbox_tasks.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="Warning!",message="you must select the task.")

#create gui
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

Listbox_tasks=tkinter.Listbox(frame_tasks,height=15,width=60)
Listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks=tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

entry_task = tkinter.Entry(root,width=50)
entry_task.pack()
button_add_task =tkinter.Button(root,text="Add Task",width=30,command=add_task)
button_add_task.pack(side=tkinter.LEFT)


button_delete_task =tkinter.Button(root,text="Delete",width=30,command=delete_task)
button_delete_task.pack(side=tkinter.RIGHT)
root.mainloop()

           
