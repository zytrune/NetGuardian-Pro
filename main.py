import customtkinter as ctk
from modules.system import get_system_info

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("NetGuardian AI")
app.geometry("1200x700")

# Sidebar
sidebar = ctk.CTkFrame(app, width=220, corner_radius=0)
sidebar.pack(side="left", fill="y")

logo = ctk.CTkLabel(
    sidebar,
    text="NetGuardian AI",
    font=("Arial", 22, "bold")
)
logo.pack(pady=30)

buttons = [
    "Dashboard",
    "Network",
    "Scanner",
    "Reports",
    "Settings",
    "Exit"
]

for item in buttons:
    btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=180,
        height=40
    )
    btn.pack(pady=8)

# Main Content
content = ctk.CTkFrame(app)
content.pack(side="right", fill="both", expand=True)

title = ctk.CTkLabel(
    content,
    text="Dashboard",
    font=("Arial", 30, "bold")
)
title.pack(pady=20)

# Get system info
system_info = get_system_info()

info_text = ""

for key, value in system_info.items():
    info_text += f"{key}: {value}\n"

info_label = ctk.CTkLabel(
    content,
    text=info_text,
    font=("Consolas", 18),
    justify="left"
)
info_label.pack(pady=20)

app.mainloop()