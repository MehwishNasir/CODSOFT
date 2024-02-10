import tkinter as tk
root = tk.Tk()
root.title("Calculator By Mehwish Nasir")

root.geometry("450x400")
root.configure(bg="grey")
root.maxsize(500,500)

#functions
def button_click(number):
    a = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END, str(a) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
        value = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)


#entry widget 
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15) 

#buttons
buttons = [
    ("7", 1, 0,"lightgrey"), ("8", 1, 1,"lightgrey"), ("9", 1, 2,"lightgrey"), ("/", 1, 3,"lightgrey"),
    ("4", 2, 0,"lightgrey"), ("5", 2, 1,"lightgrey"), ("6", 2, 2,"lightgrey"), ("*", 2, 3,"lightgrey"),
    ("1", 3, 0,"lightgrey"), ("2", 3, 1,"lightgrey"), ("3", 3, 2,"lightgrey"), ("-", 3, 3,"lightgrey"),
    ("0", 4, 0,"lightgrey"), ("C", 4, 1,"lightgrey"), ("=", 4, 2,"lightgrey"), ("+", 4, 3 ,"lightgrey")
]

#loop for creating and placing buttons
for (text, row, col,color) in buttons:
    if text.isdigit() or text == ".":
        button = tk.Button(root, text=text, padx=40, pady=20,bg=color, command=lambda t=text: button_click(t))
    elif text == "C":
        button = tk.Button(root, text=text, padx=38, pady=20,bg=color, command=button_clear)
    elif text == "=":
        button = tk.Button(root, text=text, padx=50, pady=20,bg=color, command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=41, bg=color,pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)  # Add padding to buttons for better spacing


root.mainloop()
