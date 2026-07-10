"""
NetGuardian Pro - Diagnostics Page
Provides network diagnostic tools (non-blocking).
"""

import tkinter as tk
from tkinter import scrolledtext
import threading

from ui.styles import COLORS, FONTS
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

        self.ping_button = tk.Button(
            tools_frame,
            text="Ping",
            command=self._start_ping_thread,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        self.ping_button.pack(side="left", padx=5)

        self.dns_button = tk.Button(
            tools_frame,
            text="DNS Lookup",
            command=self._start_dns_thread,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        self.dns_button.pack(side="left", padx=5)

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
    # Thread Starters
    # ==========================
    def _start_ping_thread(self):
        thread = threading.Thread(target=self._handle_ping)
        thread.daemon = True
        thread.start()

    def _start_dns_thread(self):
        thread = threading.Thread(target=self._handle_dns)
        thread.daemon = True
        thread.start()

    # ==========================
    # Handlers (Background)
    # ==========================
    def _handle_ping(self):
        host = self.entry.get().strip()
        if not host:
            return

        self._set_buttons_state("disabled")
        self._update_output("Running ping...\n\n")

        result = run_ping(host)

        self._update_output(result)
        self._set_buttons_state("normal")

    def _handle_dns(self):
        domain = self.entry.get().strip()
        if not domain:
            return

        self._set_buttons_state("disabled")
        self._update_output("Running DNS lookup...\n\n")

        result = dns_lookup(domain)

        self._update_output(result)
        self._set_buttons_state("normal")

    # ==========================
    # Safe UI Updates
    # ==========================
    def _update_output(self, text):
        def update():
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, text)

        self.after(0, update)

    def _set_buttons_state(self, state):
        def update():
            self.ping_button.config(state=state)
            self.dns_button.config(state=state)

        self.after(0, update)