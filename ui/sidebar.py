"""
NetGuardian Pro - Modern Sidebar
"""

import tkinter as tk
from ui.styles import COLORS, FONTS


class Sidebar(tk.Frame):
    def __init__(self, parent, switch_page):
        super().__init__(parent, bg=COLORS["bg_sidebar"], width=220)

        self.switch_page = switch_page
        self.pack_propagate(False)

        self.active_button = None
        self.buttons = {}

        self._create_logo()
        self._create_navigation()

    def _create_logo(self):
        logo_frame = tk.Frame(self, bg=COLORS["bg_sidebar"])
        logo_frame.pack(pady=40)

        title = tk.Label(
            logo_frame,
            text="🛡 NetGuardian",
            bg=COLORS["bg_sidebar"],
            fg=COLORS["accent"],
            font=("Segoe UI", 18, "bold")
        )
        title.pack()

        subtitle = tk.Label(
            logo_frame,
            text="Pro v1.1",
            bg=COLORS["bg_sidebar"],
            fg=COLORS["text_secondary"],
            font=("Segoe UI", 10)
        )
        subtitle.pack()

    def _create_navigation(self):
        nav_frame = tk.Frame(self, bg=COLORS["bg_sidebar"])
        nav_frame.pack(fill="both", expand=True)

        pages = [
            "Dashboard",
            "Network",
            "Diagnostics",
            "Scanner",
            "Security",
            "Reports"
        ]

        for page in pages:
            btn = tk.Label(
                nav_frame,
                text=page,
                bg=COLORS["bg_sidebar"],
                fg=COLORS["text_primary"],
                font=FONTS["body"],
                anchor="w",
                padx=25,
                pady=14,
                cursor="hand2"
            )

            btn.pack(fill="x", pady=2)

            btn.bind("<Button-1>", lambda e, p=page: self._on_click(p))
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1e293b"))
            btn.bind("<Leave>", lambda e, b=btn: self._reset_hover(b))

            self.buttons[page] = btn

    def _on_click(self, page):
        self.switch_page(page)
        self._set_active(page)

    def _set_active(self, page):
        for name, btn in self.buttons.items():
            if name == page:
                btn.config(bg=COLORS["accent"], fg="white")
                self.active_button = btn
            else:
                btn.config(bg=COLORS["bg_sidebar"], fg=COLORS["text_primary"])

    def _reset_hover(self, button):
        if button != self.active_button:
            button.config(bg=COLORS["bg_sidebar"])