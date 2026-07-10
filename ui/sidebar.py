"""
NetGuardian Pro - Sidebar Component
Creates the left navigation panel.
"""

import tkinter as tk
from ui.styles import COLORS, FONTS, LAYOUT


class Sidebar(tk.Frame):
    def __init__(self, parent, switch_page):
        super().__init__(
            parent,
            bg=COLORS["bg_sidebar"],
            width=LAYOUT["sidebar_width"]
        )

        self.switch_page = switch_page
        self.pack_propagate(False)

        self._create_logo_section()
        self._create_navigation()

    def _create_logo_section(self):
        logo_frame = tk.Frame(self, bg=COLORS["bg_sidebar"])
        logo_frame.pack(pady=30)

        app_title = tk.Label(
            logo_frame,
            text="🛡 NetGuardian Pro",
            bg=COLORS["bg_sidebar"],
            fg=COLORS["accent"],
            font=FONTS["subtitle"]
        )
        app_title.pack()

    def _create_navigation(self):
        nav_frame = tk.Frame(self, bg=COLORS["bg_sidebar"])
        nav_frame.pack(pady=20)

        buttons = [
            "Dashboard",
            "Network",
            "Diagnostics",
            "Scanner",
            "Reports",
            "Settings"
        ]

        for name in buttons:
            btn = tk.Button(
                nav_frame,
                text=name,
                bg=COLORS["bg_sidebar"],
                fg=COLORS["text_primary"],
                font=FONTS["body"],
                activebackground=COLORS["accent"],
                activeforeground="white",
                bd=0,
                relief="flat",
                padx=20,
                pady=10,
                anchor="w",
                cursor="hand2",
                command=lambda n=name: self.switch_page(n)
            )
            btn.pack(fill="x", pady=5)