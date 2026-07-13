"""
NetGuardian Pro - Stat Cards Component
Reusable dashboard information cards.
"""

import tkinter as tk
from ui.styles import COLORS, FONTS, LAYOUT


class StatCard(tk.Frame):
    def __init__(self, parent, title, unit="%"):
        super().__init__(
            parent,
            bg="#1e293b",
            width=LAYOUT["card_width"],
            height=LAYOUT["card_height"]
        )

        self.pack_propagate(False)

        self.unit = unit

        # Title
        self.title_label = tk.Label(
            self,
            text=title,
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"]
        )
        self.title_label.pack(pady=(15, 5))

        # Value
        self.value_label = tk.Label(
            self,
            text="0" + unit,
            bg="#1e293b",
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        self.value_label.pack()

    def update_value(self, value):
        if self.unit == "%":
            text = f"{value:.1f}{self.unit}"
        else:
            text = f"{value}"

        self.value_label.config(text=text)

        # Color logic
        if self.unit == "%":
            if value < 60:
                color = COLORS["success"]
            elif value < 85:
                color = COLORS["warning"]
            else:
                color = COLORS["danger"]

            self.value_label.config(fg=color)