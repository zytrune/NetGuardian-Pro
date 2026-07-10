"""
NetGuardian Pro - Reports Page
Generate and save system reports.
"""

import tkinter as tk
from tkinter import scrolledtext
import threading

from ui.styles import COLORS, FONTS
from modules.reports import generate_report, save_report


class ReportsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self._create_header()
        self._create_controls()
        self._create_output()

    # ==========================
    # Header
    # ==========================
    def _create_header(self):
        header = tk.Label(
            self,
            text="System Reports",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        header.pack(pady=20)

    # ==========================
    # Controls
    # ==========================
    def _create_controls(self):
        controls = tk.Frame(self, bg=COLORS["bg_main"])
        controls.pack(pady=10)

        self.generate_btn = tk.Button(
            controls,
            text="Generate Report",
            command=self._start_generate_thread,
            bg=COLORS["accent"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2"
        )
        self.generate_btn.pack(side="left", padx=10)

        self.save_btn = tk.Button(
            controls,
            text="Save Report",
            command=self._save_report,
            bg=COLORS["success"],
            fg="white",
            font=FONTS["body"],
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2",
            state="disabled"
        )
        self.save_btn.pack(side="left", padx=10)

    # ==========================
    # Output Area
    # ==========================
    def _create_output(self):
        self.output = scrolledtext.ScrolledText(
            self,
            width=110,
            height=25,
            bg="#111827",
            fg="white",
            font=("Consolas", 10)
        )
        self.output.pack(pady=20)

        self.status_label = tk.Label(
            self,
            text="",
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["small"]
        )
        self.status_label.pack()

    # ==========================
    # Threading
    # ==========================
    def _start_generate_thread(self):
        thread = threading.Thread(target=self._generate_report, daemon=True)
        thread.start()

    def _generate_report(self):
        self._update_status("Generating report...")
        self.generate_btn.config(state="disabled")

        report = generate_report()

        def update_ui():
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, report)

            self.generate_btn.config(state="normal")
            self.save_btn.config(state="normal")
            self._update_status("Report generated successfully.")

        self.after(0, update_ui)

    # ==========================
    # Save Report
    # ==========================
    def _save_report(self):
        report_text = self.output.get("1.0", tk.END)

        if not report_text.strip():
            return

        filepath = save_report(report_text)
        self._update_status(f"Saved to: {filepath}")

    # ==========================
    # Status Helper
    # ==========================
    def _update_status(self, message):
        self.status_label.config(text=message)