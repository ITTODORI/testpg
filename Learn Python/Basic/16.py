import tkinter as tk
from tkinter import ttk

# initialize the main application window
app = tk.Tk()
app.title("Mobile App")
app.configure(bg="white")
app.geometry("480x853")
app.resizable(False, False)

EMAIL = tk.StringVar()
PASSWORD = tk.StringVar()

# Frame
input_frame = ttk.Frame(app, width=480, height=853)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Components
# - Email
mail_label = ttk.Label(input_frame, text="Email")
mail_label.pack(padx=10,fill="x",expand=True)

# Entry
mail_entry = ttk.Entry(input_frame, textvariable=EMAIL)
mail_entry.pack(padx=10,fill="x",expand=True)

# - Password
pass_label = ttk.Label(input_frame, text="Email")
pass_label.pack(padx=10,fill="x",expand=True)

pass_entry = ttk.Entry(input_frame, textvariable=PASSWORD)
pass_entry.pack(padx=10,fill="x",expand=True)

# Button
def button_click():
    '''function Notice Messager'''
    notice = f"Login Succes {EMAIL.get()}"
    showinfo(title="Login Notice",message=notice)

click_button = ttk.Button(input_frame,text="Login",command=button_click)
click_button.pack(fill='x', expand=True,pady=10,padx=10)


app.mainloop()