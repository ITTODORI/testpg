# GUI : Graphical User Interface
import tkinter as tk

app = tk.Tk()
app.configure(bg="black")
app.geometry("1080x1920")
app.resizable(False,False)
app.title("Mini Apps")

EMAIL = ttk.StringVar()
PASSWORD = ttk.StringVar()
# Frame Input
input_frame = ttk.Frame(app)
# Place, Grid, Pack
input_frame.pack(padx=10,pady-10,fill="x",expand=True)

# Components
# Email
mail_label = ttk.Label(input_frame, text="Email")
mail_label.pack(padx=10,fill="x",expand=True)

# Entry
mail_entry = ttk.Entry(input_frame, textvariable=EMAIL)
mail_entry.pack(padx=10,fill="x",expand=True)

# Password
pass_label = ttk.Label(input_frame, text="Email")
pass_label.pack(padx=10,fill="x",expand=True)

pass_entry = ttk.Entry(input_frame, textvariable=PASSWORD)
pass_entry.pack(padx=10,fill="x",expand=True)


app.mainloop()