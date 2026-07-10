"""
NetGuardian Pro - Dashboard View
Main dashboard content area.
"""

import tkinter as tk
from datetime import datetime

from ui.styles import COLORS, FONTS, LAYOUT
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
        self._create_cards()

    def start(self):
        if not self.running:
            self.running = True
            self._update_stats()
            self._update_clock()

    def stop(self):
        self.running = False
        if self.after_id_stats:
            self.after_cancel(self.after_id_stats)
            self.after_id_stats = None
        if self.after_id_clock:
            self.after_cancel(self.after_id_clock)
            self.after_id_clock = None

    def _create_header(self):
        header_frame = tk.Frame(self, bg=COLORS["bg_main"])
        header_frame.pack(fill="x", padx=LAYOUT["padding"], pady=20)

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

    def _create_cards(self):
        self.cards_frame = tk.Frame(self, bg=COLORS["bg_main"])
        self.cards_frame.pack(padx=LAYOUT["padding"], pady=10)

        self.cpu_card = StatCard(self.cards_frame, "CPU Usage")
        self.cpu_card.grid(row=0, column=0, padx=15, pady=15)

        self.ram_card = StatCard(self.cards_frame, "RAM Usage")
        self.ram_card.grid(row=0, column=1, padx=15, pady=15)

        self.disk_card = StatCard(self.cards_frame, "Disk Usage")
        self.disk_card.grid(row=0, column=2, padx=15, pady=15)

        self.uptime_card = StatCard(self.cards_frame, "System Uptime", unit="")
        self.uptime_card.grid(row=1, column=0, padx=15, pady=15)

    def _update_stats(self):
        if not self.running:
            return

        cpu = get_cpu_usage()
        ram = get_ram_usage()
        disk = get_disk_usage()
        uptime = get_system_uptime()

        self.cpu_card.update_value(cpu)
        self.ram_card.update_value(ram)
        self.disk_card.update_value(disk)
        self.uptime_card.update_value(uptime)

        self.after_id_stats = self.after(1000, self._update_stats)

    def _update_clock(self):
        if not self.running:
            return

        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)

        self.after_id_clock = self.after(1000, self._update_clock)