"""
NetGuardian Pro - Scanner Page
Enhanced Port Scanner UI with custom port range.
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import threading

from ui.styles import COLORS, FONTS
from modules.scanner import run_port_scan


class ScannerPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self._create_header()
        self._create_controls()
        self._create_output_area()

    def _create_header(self):
        header = tk.Label(
            self,
            text="Cybersecurity Port Scanner",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        header.pack(pady=20)

    def _create_controls(self):
        controls_frame = tk.Frame(self, bg=COLORS["bg_main"])
        controls_frame.pack(pady=10)

        # Target
        tk.Label(
            controls_frame,
            text="Target:",
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"]
        ).grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(controls_frame, font=FONTS["body"], width=20)
        self.entry.insert(0, "localhost")
        self.entry.grid(row=0, column=1, padx=5)

        # Start Port
        tk.Label(
            controls_frame,
            text="Start Port:",
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"]
        ).grid(row=1, column=0, padx=5)

        self.start_port_entry = tk.Entry(controls_frame, width=8)
        self.start_port_entry.insert(0, "1")
        self.start_port_entry.grid(row=1, column=1, sticky="w")

        # End Port
        tk.Label(
            controls_frame,
            text="End Port:",
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"]
        ).grid(row=1, column=1, padx=70, sticky="w")

        self.end_port_entry = tk.Entry(controls_frame, width=8)
        self.end_port_entry.insert(0, "1024")
        self.end_port_entry.grid(row=1, column=1, padx=140, sticky="w")

        # Scan Button
        self.scan_button = tk.Button(
            controls_frame,
            text="Scan Ports",
            command=self._start_scan_thread,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2"
        )
        self.scan_button.grid(row=0, column=2, rowspan=2, padx=20)

        # Progress bar
        self.progress = ttk.Progressbar(
            self,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        self.progress.pack(pady=10)

    def _create_output_area(self):
        self.output = scrolledtext.ScrolledText(
            self,
            width=100,
            height=20,
            bg="#111827",
            fg="white",
            font=("Consolas", 10)
        )
        self.output.pack(pady=15)

    def _start_scan_thread(self):
        thread = threading.Thread(target=self._run_scan, daemon=True)
        thread.start()

    def _run_scan(self):
        target = self.entry.get().strip()

        try:
            start_port = int(self.start_port_entry.get())
            end_port = int(self.end_port_entry.get())
        except ValueError:
            self._update_output("Invalid port numbers.\n")
            return

        if not target:
            return

        self.scan_button.config(state="disabled")
        self.progress["value"] = 0
        self._update_output(f"Scanning {target} from port {start_port} to {end_port}...\n")

        results = run_port_scan(target, start_port, end_port, self._update_progress)

        def finish():
            self.output.insert(tk.END, results)
            self.scan_button.config(state="normal")
            self.progress["value"] = 100

        self.after(0, finish)

    def _update_progress(self, value):
        def update():
            self.progress["value"] = value
        self.after(0, update)

    def _update_output(self, text):
        def update():
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, text)
        self.after(0, update)