"""
NetGuardian Pro - Live Security Overview
"""

import tkinter as tk

from ui.styles import COLORS, FONTS
from modules.intelligence import calculate_security_score


class SecurityPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg_main"])

        self.running = False
        self.after_id = None

        self._create_header()
        self._create_score_section()
        self._create_recommendation_card()

    # ==========================
    # Header
    # ==========================
    def _create_header(self):
        header = tk.Label(
            self,
            text="Security Overview",
            bg=COLORS["bg_main"],
            fg=COLORS["text_primary"],
            font=FONTS["title"]
        )
        header.pack(pady=30)

    # ==========================
    # Score Section
    # ==========================
    def _create_score_section(self):
        self.score_label = tk.Label(
            self,
            text="--",
            bg=COLORS["bg_main"],
            fg=COLORS["accent"],
            font=("Segoe UI", 70, "bold")
        )
        self.score_label.pack()

        self.level_label = tk.Label(
            self,
            text="--",
            bg=COLORS["bg_main"],
            fg=COLORS["text_secondary"],
            font=FONTS["subtitle"]
        )
        self.level_label.pack(pady=10)

    # ==========================
    # Recommendation Card
    # ==========================
    def _create_recommendation_card(self):
        self.card = tk.Frame(
            self,
            bg=COLORS["bg_card"],
            padx=30,
            pady=30
        )
        self.card.pack(fill="x", pady=40)

        title = tk.Label(
            self.card,
            text="Recommendations",
            bg=COLORS["bg_card"],
            fg=COLORS["text_primary"],
            font=FONTS["subtitle"]
        )
        title.pack(anchor="w", pady=(0, 15))

        self.recommendations_label = tk.Label(
            self.card,
            text="",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font=FONTS["body"],
            justify="left"
        )
        self.recommendations_label.pack(anchor="w")

    # ==========================
    # Lifecycle
    # ==========================
    def start(self):
        if not self.running:
            self.running = True
            self._update_security()

    def stop(self):
        self.running = False
        if self.after_id:
            self.after_cancel(self.after_id)

    # ==========================
    # Live Update
    # ==========================
    def _update_security(self):
        if not self.running:
            return

        result = calculate_security_score()

        score = result["score"]
        level = result["level"]
        recommendations = result["recommendations"]

        self.score_label.config(text=str(score))

        if level == "Low":
            color = COLORS["success"]
        elif level == "Moderate":
            color = COLORS["warning"]
        else:
            color = COLORS["danger"]

        self.level_label.config(
            text=f"Risk Level: {level}",
            fg=color
        )

        if recommendations:
            text = ""
            for item in recommendations:
                text += f"• {item}\n"
        else:
            text = "• System security posture is healthy."

        self.recommendations_label.config(text=text)

        self.after_id = self.after(5000, self._update_security)