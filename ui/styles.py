"""
NetGuardian Pro - UI Styles
Central styling configuration for the entire application.
All colors, fonts, and layout constants are defined here.
"""

# ==============================
# 🎨 COLOR PALETTE
# ==============================

COLORS = {
    # Main backgrounds
    "bg_main": "#0f172a",        # Dark navy background
    "bg_sidebar": "#111827",     # Sidebar slightly darker
    "bg_card": "#1f2937",        # Card background
    
    # Accent colors
    "accent": "#3b82f6",         # Blue accent
    "success": "#22c55e",        # Green
    "warning": "#f59e0b",        # Orange
    "danger": "#ef4444",         # Red
    
    # Text colors
    "text_primary": "#f9fafb",   # Almost white
    "text_secondary": "#9ca3af", # Soft gray
}

# ==============================
# 🔤 FONTS
# ==============================

FONTS = {
    "title": ("Segoe UI", 20, "bold"),
    "subtitle": ("Segoe UI", 14, "bold"),
    "body": ("Segoe UI", 12),
    "small": ("Segoe UI", 10),
}

# ==============================
# 📏 LAYOUT CONSTANTS
# ==============================

LAYOUT = {
    "sidebar_width": 220,
    "card_width": 260,
    "card_height": 120,
    "padding": 15,
}