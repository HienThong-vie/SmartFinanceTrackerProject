import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
from colors_scheme import COLORS
from core.data_manager import get_transaction
from core.algorithm import analyze_budgets

def build_chart_page(frame,data):
    #data needed
    analysis_data = analyze_budgets(data)
    #function
    def show_donut():
        for widget in donut_frame.winfo_children():
            widget.destroy()
        build_donut_chart()
        donut_frame.pack(fill="both",expand=True,padx=20,pady=15 )
        spending_breakdown_button.configure(bg=COLORS["accent"])
        monthly_trend_button.configure(bg=COLORS["bg_sidebar"])
        bar_frame.pack_forget()
    def show_bar():
        bar_frame.pack(fill="both",expand=True,padx=20,pady=15)
        monthly_trend_button.configure(bg=COLORS["accent"])
        spending_breakdown_button.configure(bg=COLORS["bg_sidebar"])
        donut_frame.pack_forget()
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
        text="🍩 Spending Breakdown",
        command=show_donut,
        bg=None,
        fg=COLORS["text_light"],
        font=("Segoe UI", 10,"bold"),
        cursor="hand2",
    )
    monthly_trend_button = tk.Button(
        tab_frame,
        text="📊 Monthly Trend",
        command=show_bar,
        bg=None,
        fg=COLORS["text_light"],
        font=("Segoe UI", 10,"bold"),
        cursor="hand2",
    )
    chart_container = tk.Frame(
        frame,
        bg=COLORS["bg_main"]
    )
    donut_frame = tk.Frame(
        chart_container,
    )
    bar_frame = tk.Frame(
        chart_container
    )
    #placing
    page_title.pack(anchor="w",padx=20,pady=15)
    tab_frame.pack(fill="x",padx=20,pady=5)

    spending_breakdown_button.grid(row=0,column=0,sticky="ew",padx=10)
    monthly_trend_button.grid(row=0,column=1,sticky="ew",padx=10)

    tab_frame.columnconfigure(0, weight=1) # all weight 1 means all 2 columns will take up equal space until there is no blank
    tab_frame.columnconfigure(1, weight=1)

    chart_container.pack(fill="both", expand=True)

    donut_frame.pack(fill="both",padx=20,pady=15)
    bar_frame.pack(fill="both",padx=20,pady=15)
    #charts
    if not analysis_data:
        tk.Label(
            chart_container,
            text="No budget data available",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            font = ("Segoe UI", 13)
        ).pack(fill="x",pady=5)
    else:
        def build_donut_chart():
            fig, ax = plt.subplots(figsize=(6, 4))
            labels = []
            sizes = []
            for analysis in analysis_data:
                spent = analysis_data[analysis]["spent"]
                if spent > 0:
                    sizes.append(spent)
                    labels.append(analysis)
            
            #draw donut
            def autopct_format(pct):
                return f"{pct:.1f}%" if pct > 3 else ""
            wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct=autopct_format,
            wedgeprops=dict(width=0.6),
            pctdistance=0.75
            )
            ax.set_title("Spending by Category")
            ax.axis("equal")
            for text in autotexts:
                text.set_fontsize(9)
            #setting donut inside the page 
            canvas = FigureCanvasTkAgg(fig, master=donut_frame) # master means the parent frame we place this canvas
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both")
            #adding color to this donut chart - transparent
            fig.patch.set_facecolor(COLORS["bg_main"])
            ax.set_facecolor(COLORS["bg_main"])
            return
    #function call
    show_donut()
