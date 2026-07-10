"""
NetGuardian Pro - Network Page
Displays network information without blocking the UI.
"""

import tkinter as tk
import threading

from ui.styles import COLORS, FONTS
from modules.network import (
    get_local_ip,
    get_public_ip,
    get_network_status,
    get_network_usage,
)


class NetworkPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self.running = False
        self.quick_after_id = None
        self.external_after_id = None
        self.external_refresh_in_progress = False

        self._create_header()
        self._create_content()

    # ==========================
    # Lifecycle Control
    # ==========================
    def start(self):
        if not self.running:
            self.running = True
            self._update_quick_info()
            self._refresh_external_info()

    def stop(self):
        self.running = False

        if self.quick_after_id:
            self.after_cancel(self.quick_after_id)
            self.quick_after_id = None

        if self.external_after_id:
            self.after_cancel(self.external_after_id)
            self.external_after_id = None

    # ==========================
    # Header
    # ==========================
    def _create_header(self):
        header = tk.Label(
            self,
            text="Network Overview",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        header.pack(pady=20)

    # ==========================
    # Content
    # ==========================
    def _create_content(self):
        self.content_frame = tk.Frame(self, bg=COLORS["bg_main"])
        self.content_frame.pack(pady=20)

        self.local_ip_label = tk.Label(
            self.content_frame,
            text="Local IP: Loading...",
            font=FONTS["body"],
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"]
        )
        self.local_ip_label.pack(pady=5)

        self.public_ip_label = tk.Label(
            self.content_frame,
            text="Public IP: Loading...",
            font=FONTS["body"],
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"]
        )
        self.public_ip_label.pack(pady=5)

        self.status_label = tk.Label(
            self.content_frame,
            text="Status: Checking...",
            font=FONTS["body"],
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"]
        )
        self.status_label.pack(pady=5)

        self.usage_label = tk.Label(
            self.content_frame,
            text="Sent: -- MB | Received: -- MB",
            font=FONTS["body"],
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"]
        )
        self.usage_label.pack(pady=5)

    # ==========================
    # Fast Updates (Local Only)
    # ==========================
    def _update_quick_info(self):
        if not self.running:
            return

        local_ip = get_local_ip()
        sent, received = get_network_usage()

        self.local_ip_label.config(text=f"Local IP: {local_ip}")
        self.usage_label.config(text=f"Sent: {sent} MB | Received: {received} MB")

        self.quick_after_id = self.after(1000, self._update_quick_info)

    # ==========================
    # Slow Updates (Background Thread)
    # ==========================
    def _refresh_external_info(self):
        if not self.running or self.external_refresh_in_progress:
            return

        self.external_refresh_in_progress = True
        self.public_ip_label.config(text="Public IP: Loading...")
        self.status_label.config(text="Status: Checking...", fg=COLORS["text_secondary"])

        thread = threading.Thread(target=self._fetch_external_info, daemon=True)
        thread.start()

    def _fetch_external_info(self):
        public_ip = get_public_ip()
        status = get_network_status()

        def update_ui():
            self.external_refresh_in_progress = False

            if not self.running:
                return

            self.public_ip_label.config(text=f"Public IP: {public_ip}")

            if status == "Connected":
                self.status_label.config(text="Status: Connected", fg=COLORS["success"])
            else:
                self.status_label.config(text="Status: Disconnected", fg=COLORS["danger"])

            self.external_after_id = self.after(30000, self._refresh_external_info)

        self.after(0, update_ui)