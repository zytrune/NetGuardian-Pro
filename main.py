"""
NetGuardian Pro
Main Application Entry Point
"""

import tkinter as tk

from ui.styles import COLORS
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.network_page import NetworkPage
from ui.diagnostics_page import DiagnosticsPage
from ui.reports_page import ReportsPage

class NetGuardianApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NetGuardian Pro v1.1")
        self.geometry("1100x650")
        self.minsize(900, 600)
        self.configure(bg=COLORS["bg_main"])

        self._create_layout()
        self.show_page("Dashboard")

    def _create_layout(self):
        # Sidebar
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.pack(side="left", fill="y")

        # Container for pages
        self.container = tk.Frame(self, bg=COLORS["bg_main"])
        self.container.pack(side="right", fill="both", expand=True)

        # Store pages
        self.pages = {}

        # Create pages
        self.pages["Dashboard"] = Dashboard(self.container)
        self.pages["Network"] = NetworkPage(self.container)
        self.pages["Diagnostics"] = DiagnosticsPage(self.container)
        self.pages["Reports"] = ReportsPage(self.container)
    def show_page(self, page_name):
        # Stop and hide all pages
        for page in self.pages.values():
            if hasattr(page, "stop"):
                page.stop()
            page.pack_forget()

        # Show selected page
        if page_name in self.pages:
            page = self.pages[page_name]
            page.pack(fill="both", expand=True)

            if hasattr(page, "start"):
                page.start()


if __name__ == "__main__":
    app = NetGuardianApp()
    app.mainloop()