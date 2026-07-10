"""
NetGuardian Pro
Main Application Entry Point
"""

import tkinter as tk

from modules.logger import log_info, log_error
from ui.styles import COLORS
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.network_page import NetworkPage
from ui.diagnostics_page import DiagnosticsPage
from ui.scanner_page import ScannerPage
from ui.reports_page import ReportsPage


class NetGuardianApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NetGuardian Pro v1.1")
        self.geometry("1100x650")
        self.minsize(900, 600)
        self.configure(bg=COLORS["bg_main"])

        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._create_layout()
        self.show_page("Dashboard")

        log_info("Application started.")

    def _create_layout(self):
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.pack(side="left", fill="y")

        self.container = tk.Frame(self, bg=COLORS["bg_main"])
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {
            "Dashboard": Dashboard(self.container),
            "Network": NetworkPage(self.container),
            "Diagnostics": DiagnosticsPage(self.container),
            "Scanner": ScannerPage(self.container),
            "Reports": ReportsPage(self.container),
        }

    def show_page(self, page_name):
        for page in self.pages.values():
            if hasattr(page, "stop"):
                page.stop()
            page.pack_forget()

        page = self.pages.get(page_name)

        if page is None:
            log_error(f"Unknown page requested: {page_name}")
            return

        page.pack(fill="both", expand=True)

        if hasattr(page, "start"):
            page.start()

        log_info(f"Opened page: {page_name}")

    def _on_close(self):
        for page in self.pages.values():
            if hasattr(page, "stop"):
                page.stop()

        log_info("Application closed.")
        self.destroy()


if __name__ == "__main__":
    try:
        app = NetGuardianApp()
        app.mainloop()
    except Exception:
        log_error("Unhandled exception occurred.", include_traceback=True)
        raise