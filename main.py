"""
NetGuardian Pro
Main Application Entry Point
"""

import tkinter as tk

from ui.styles import COLORS
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard


class NetGuardianApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("NetGuardian Pro v1.1")
        self.geometry("1100x650")
        self.minsize(900, 600)
        self.configure(bg=COLORS["bg_main"])

        # Layout Structure
        self._create_layout()

    def _create_layout(self):
        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # Main Content Area
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side="right", fill="both", expand=True)


if __name__ == "__main__":
    app = NetGuardianApp()
    app.mainloop()