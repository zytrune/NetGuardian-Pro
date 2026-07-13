"""
NetGuardian Pro - Structured Dashboard
"""

import tkinter as tk
from datetime import datetime

from ui.styles import COLORS, FONTS
from ui.cards import StatCard
from modules.system import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage,
    get_system_uptime,
)


class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self.running = False
        self.after_id_stats = None
        self.after_id_clock = None

        self._create_header()
        self._create_sections()

    def _create_header(self):
        header_frame = tk.Frame(self, bg=COLORS["bg_main"])
        header_frame.pack(fill="x", pady=(0, 25))

        title = tk.Label(
            header_frame,
            text="Dashboard",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        title.pack(side="left")

        self.clock_label = tk.Label(
            header_frame,
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"]
        )
        self.clock_label.pack(side="right")

    def _create_sections(self):

        # Performance Section
        perf_section = tk.Frame(
            self,
            bg=COLORS["bg_card"],
            padx=30,
            pady=30
        )
        perf_section.pack(fill="x", pady=(0, 30))

        perf_title = tk.Label(
            perf_section,
            text="Performance",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font=FONTS["subtitle"]
        )
        perf_title.pack(anchor="w", pady=(0, 20))

        perf_grid = tk.Frame(perf_section, bg=COLORS["bg_card"])
        perf_grid.pack()

        self.cpu_card = StatCard(perf_grid, "CPU Usage")
        self.ram_card = StatCard(perf_grid, "RAM Usage")
        self.disk_card = StatCard(perf_grid, "Disk Usage")

        self.cpu_card.grid(row=0, column=0, padx=25)
        self.ram_card.grid(row=0, column=1, padx=25)
        self.disk_card.grid(row=0, column=2, padx=25)

        # System Section
        sys_section = tk.Frame(
            self,
            bg=COLORS["bg_card"],
            padx=30,
            pady=30
        )
        sys_section.pack(fill="x")

        sys_title = tk.Label(
            sys_section,
            text="System Status",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font=FONTS["subtitle"]
        )
        sys_title.pack(anchor="w", pady=(0, 20))

        self.uptime_card = StatCard(sys_section, "System Uptime", unit="")
        self.uptime_card.pack()

    def start(self):
        if not self.running:
            self.running = True
            self._update_stats()
            self._update_clock()

    def stop(self):
        self.running = False
        if self.after_id_stats:
            self.after_cancel(self.after_id_stats)
        if self.after_id_clock:
            self.after_cancel(self.after_id_clock)

    def _update_stats(self):
        if not self.running:
            return

        self.cpu_card.update_value(get_cpu_usage())
        self.ram_card.update_value(get_ram_usage())
        self.disk_card.update_value(get_disk_usage())
        self.uptime_card.update_value(get_system_uptime())

        self.after_id_stats = self.after(1000, self._update_stats)

    def _update_clock(self):
        if not self.running:
            return

        self.clock_label.config(
            text=datetime.now().strftime("%H:%M:%S")
        )

        self.after_id_clock = self.after(1000, self._update_clock)