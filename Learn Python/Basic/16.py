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
pass_label = ttk.Label(input_frame, text="Password")
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

# MOBILE APP
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

# Configuration: Luxury & Clean Theme
ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")

class RamadhanApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Ramadhan Berkah - App")
        self.geometry("450x850")
        self.configure(fg_color="#F8F9FA") # Soft Off-white background

        # --- SCROLLABLE CONTAINER ---
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=5, pady=5)

        # --- HEADER BANNER ---
        self.header_banner = ctk.CTkFrame(self.main_container, height=180, corner_radius=15, fg_color="#4A148C")
        self.header_banner.pack(fill="x", pady=(0, 10))
        
        self.header_label = ctk.CTkLabel(
            self.header_banner, 
            text="RAMADHAN BERKAH", 
            font=ctk.CTkFont(family="Inter", size=26, weight="bold"),
            text_color="white"
        )
        self.header_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- LOGIN SECTION ---
        self.login_card = ctk.CTkFrame(self.main_container, corner_radius=15, fg_color="white", border_width=1, border_color="#E0E0E0")
        self.login_card.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(self.login_card, text="Quick Login", font=("Inter", 16, "bold")).pack(pady=(15, 10))
        
        self.email_entry = ctk.CTkEntry(self.login_card, placeholder_text="Email", width=350, height=45, corner_radius=10)
        self.email_entry.pack(pady=5, padx=20)
        
        self.pass_entry = ctk.CTkEntry(self.login_card, placeholder_text="Password", show="*", width=350, height=45, corner_radius=10)
        self.pass_entry.pack(pady=5, padx=20)

        self.login_btn = ctk.CTkButton(
            self.login_card, 
            text="LOGIN", 
            command=self.login_action, 
            fg_color="#212121", 
            hover_color="#424242", 
            corner_radius=10, 
            font=("Inter", 14, "bold"),
            height=45
        )
        self.login_btn.pack(pady=20, padx=20, fill="x")

        # --- GRID DONASI ---
        self.grid_container = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.grid_container.pack(fill="both", expand=True, padx=5)
        self.grid_container.columnconfigure((0, 1), weight=1)

        # Items Grid
        self.create_item_card(0, 0, "Ifthar - Sahur", "Rp. 25.000")
        self.create_item_card(0, 1, "B-YAD", "Rp. 150.000")
        self.create_item_card(1, 0, "BASMALAH", "Rp. 100.000")
        self.create_item_card(1, 1, "Guru Ngaji", "Rp. 100.000")

        # --- DONATION INFO (BSI Section) ---
        self.info_card = ctk.CTkFrame(self.main_container, fg_color="#4A148C", corner_radius=15)
        self.info_card.pack(fill="x", padx=10, pady=20)
        
        ctk.CTkLabel(self.info_card, text="BSI Al Himmah Donasi", text_color="white", font=("Inter", 14)).pack(pady=(15,0))
        ctk.CTkLabel(self.info_card, text="4414410028", text_color="white", font=("Inter", 24, "bold")).pack(pady=(5, 15))

    def create_item_card(self, row, col, title, price):
        # Card Base
        card = ctk.CTkFrame(self.grid_container, corner_radius=15, fg_color="white", border_width=1, border_color="#EEEEEE")
        card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

        # Image Placeholder
        img_placeholder = ctk.CTkFrame(card, height=120, corner_radius=10, fg_color="#F5F5F5")
        img_placeholder.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(img_placeholder, text="🌙", font=("Inter", 32)).place(relx=0.5, rely=0.5, anchor="center")

        # Text Info
        ctk.CTkLabel(card, text=title, font=("Inter", 14, "bold"), text_color="#212121").pack(anchor="w", padx=12)
        ctk.CTkLabel(card, text=price, font=("Inter", 13, "bold"), text_color="#7B1FA2").pack(anchor="w", padx=12, pady=(0, 5))
        
        # Donate Button with Requested Hover Color
        btn = ctk.CTkButton(
            card, 
            text="Donate it", 
            height=35, 
            corner_radius=8, 
            fg_color="#4A148C",      # Deep Purple
            hover_color="#8333E4",   # Brighter Purple (Requested)
            font=("Inter", 12, "bold"),
            command=lambda t=title: self.donate_action(t)
        )
        btn.pack(pady=(5, 12), padx=12, fill="x")

    def login_action(self):
        email = self.email_entry.get()
        if email:
            messagebox.showinfo("Login Success", f"Welcome back,\n{email}")
        else:
            messagebox.showwarning("Attention", "Please enter your email to continue.")

    def donate_action(self, item_name):
        messagebox.showinfo("Donation", f"Thank you for choosing to donate to:\n{item_name}")

if __name__ == "__main__":
    app = RamadhanApp()
    app.mainloop()