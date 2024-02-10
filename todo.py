from tkinter import *
import tkinter.messagebox as msg
root = Tk()

root.title("TO-DO LIST APP")
root.geometry("500x500")
root.configure(bg="black")
root.maxsize(500,500)

#Frames
frame = Frame(root,bg="black")
title = Label(frame,text="        Enter the task : ",font=("Times New Roman",11,"bold"),fg="white",bg="black",pady=10)
frame.pack(fill=X)
title.pack(side='top',anchor='nw')
f2 = Frame(root, bg='black').pack(fill=X)
tasks = StringVar()
task_entered = Entry(frame,textvariable=tasks,font=("Arial", 6,'bold'),width=80).place(x=150,y=10,height=20)

#Functions for Button
i=1
def add_task():
    global i
    global tasks
   
    task_string = tasks.get()
    if len(task_string)==0:
        msg.showinfo("Error!","Tasks field is empty")
    elif len(task_string)!=0:
        list.insert(END,f"{i}."+task_string)
        i+=1
def dlt_task():
    ar =''
    for int in list.curselection():
        ar=list.curselection()
    i=len(ar)-1
    while(i>=0):
        list.delete(ar[i])
        i=i-1
    if len(ar)==0:    
        msg.showinfo('Error', 'No Task Selected. Cannot Delete.')
def dltall_task():
       message_box = msg.askyesno('Delete All', 'Are you sure?')  
       if message_box == True:  
           clear_list()
def clear_list():  
    list.delete(0, 'end')  
def exit():
    root.quit()

#Buttons
button1 = Button(root,text="ADD",font=("Arial",6,"bold"),command=add_task,bg="gold").place(x=10,y=45,width=150,height=20)  
button2 = Button(root,text="DELETE",font=("Arial",6,"bold"),command=dlt_task,bg="gold").place(x=170,y=45,width=150,height=20)
button3 = Button(root,text="DELETE ALL",font=("Arial",6,"bold"),command=dltall_task,bg="gold").place(x=330,y=45,width=150,height=20)     
button4 = Button(root,text="EXIT",font=("Arial",6,"bold"),command=exit,bg="gold").place(x=25,y=425,width=450,height=30)
list = Listbox(root,justify=LEFT,width=75,height=20,font="Arial 8 bold")
list.place(y=80,x=25)
root.mainloop()

