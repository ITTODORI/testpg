# GUI : Graphical User Interface
import tkinter as tk

# INIT
app = tk.Tk()
app.configure(bg="black")
app.geometry("1080x1920")
app.resizable(False,False)
app.title("Mini Apps")

# VAR
EMAIL = ttk.StringVar()
PASSWORD = ttk.StringVar()

# Frame Input
input_frame = ttk.Frame(app)
# Place, Grid, Pack
input_frame.pack(padx=10,pady-10,fill="x",expand=True)

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