import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
from colors_scheme import COLORS
from core.data_manager import get_transaction
from core.algorithm import analyze_budgets

def build_chart_page(frame,data):
    def show_donut():
        pass
    #widgets
    page_title = tk.Label(
        frame,
        text = "📈 Charts",
        bg= COLORS["bg_main"],
        fg= COLORS["text_primary"],
        font = ("Segoe UI", 18, "bold")
    )
    tab_frame = tk.Frame(
        frame,
    )
    spending_breakdown_button = tk.Button(
        tab_frame,
        text="🍩 Spending Breakdown"
    )
    monthly_trend_button = tk.Button(
        tab_frame,
        text="📊 Monthly Trend"
    )
    chart_container = tk.Frame(
        frame,
        bg = COLORS["bg_main"],
    )
    donut_frame = tk.Frame(
        chart_container,
    )
    bar_frame = tk.Frame(
        chart_container
    )
    #placing
    page_title.pack(anchor="w",padx=20,pady=15)
    #function call
    show_donut()
