"""
NetGuardian Pro - Network Page
Displays network information.
"""

import tkinter as tk
from ui.styles import COLORS, FONTS, LAYOUT
from modules.network import (
    get_local_ip,
    get_public_ip,
    get_network_status,
    get_network_usage,
)


class NetworkPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self._create_header()
        self._create_content()
        self._update_network_info()

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

        self.local_ip_label = tk.Label(self.content_frame, font=FONTS["body"], bg=COLORS["bg_main"], fg=COLORS["text_primary"])
        self.local_ip_label.pack(pady=5)

        self.public_ip_label = tk.Label(self.content_frame, font=FONTS["body"], bg=COLORS["bg_main"], fg=COLORS["text_primary"])
        self.public_ip_label.pack(pady=5)

        self.status_label = tk.Label(self.content_frame, font=FONTS["body"], bg=COLORS["bg_main"])
        self.status_label.pack(pady=5)

        self.usage_label = tk.Label(self.content_frame, font=FONTS["body"], bg=COLORS["bg_main"], fg=COLORS["text_primary"])
        self.usage_label.pack(pady=5)

    # ==========================
    # Update Network Info
    # ==========================
    def _update_network_info(self):
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        status = get_network_status()
        sent, received = get_network_usage()

        self.local_ip_label.config(text=f"Local IP: {local_ip}")
        self.public_ip_label.config(text=f"Public IP: {public_ip}")
        self.usage_label.config(text=f"Sent: {sent} MB | Received: {received} MB")

        if status == "Connected":
            self.status_label.config(text="Status: Connected", fg=COLORS["success"])
        else:
            self.status_label.config(text="Status: Disconnected", fg=COLORS["danger"])

        self.after(3000, self._update_network_info)