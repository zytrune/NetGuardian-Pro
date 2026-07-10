"""
NetGuardian Pro - Diagnostics Page
Provides network diagnostic tools.
"""

import tkinter as tk
from tkinter import scrolledtext

from ui.styles import COLORS, FONTS, LAYOUT
from modules.diagnostics import run_ping, dns_lookup


class DiagnosticsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self._create_header()
        self._create_tools()
        self._create_output_area()

    # ==========================
    # Header
    # ==========================
    def _create_header(self):
        header = tk.Label(
            self,
            text="Network Diagnostics",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        header.pack(pady=20)

    # ==========================
    # Tools Section
    # ==========================
    def _create_tools(self):
        tools_frame = tk.Frame(self, bg=COLORS["bg_main"])
        tools_frame.pack(pady=10)

        self.entry = tk.Entry(
            tools_frame,
            font=FONTS["body"],
            width=30
        )
        self.entry.pack(side="left", padx=10)

        ping_button = tk.Button(
            tools_frame,
            text="Ping",
            command=self._handle_ping,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        ping_button.pack(side="left", padx=5)

        dns_button = tk.Button(
            tools_frame,
            text="DNS Lookup",
            command=self._handle_dns,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        dns_button.pack(side="left", padx=5)

    # ==========================
    # Output Area
    # ==========================
    def _create_output_area(self):
        self.output = scrolledtext.ScrolledText(
            self,
            width=100,
            height=20,
            bg="#111827",
            fg="white",
            font=("Consolas", 10)
        )
        self.output.pack(pady=20)

    # ==========================
    # Handlers
    # ==========================
    def _handle_ping(self):
        host = self.entry.get().strip()
        if not host:
            return

        self.output.delete("1.0", tk.END)
        result = run_ping(host)
        self.output.insert(tk.END, result)

    def _handle_dns(self):
        domain = self.entry.get().strip()
        if not domain:
            return

        self.output.delete("1.0", tk.END)
        result = dns_lookup(domain)
        self.output.insert(tk.END, result)