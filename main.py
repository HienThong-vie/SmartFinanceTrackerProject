from core.data_manager import load_data
import tkinter as tk
from constants import COLORS
from gui.transactions import build_transactions_page
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwarenesreallys(1)
except:
    pass

def show_frame(frame):
    frame.tkraise()

def main():
    data = load_data()  
    root = tk.Tk()
    #root.state("zoomed")
    root.geometry("800x600")
    root.title("Smart Finance Tracker")

    #creating widgets is like buying furniture 
    content_frame = tk.Frame(
        root,
        bg = COLORS["bg_main"]
    )
    dashboard_frame = tk.Frame(
        content_frame,
        bg = COLORS["bg_main"]
    )
    transactions_frame = tk.Frame(
        content_frame,
        bg = COLORS["bg_main"]
    )
    budget_frame = tk.Frame(
        content_frame,
        bg = COLORS["bg_main"]
        
    )
    charts_frame = tk.Frame(
        content_frame,
        bg = COLORS["bg_main"]
    )
    advisor_frame = tk.Frame(
        content_frame,
        bg = COLORS["bg_main"]
    )
    sidebar_frame = tk.Frame(
        root,
        bg = COLORS["bg_sidebar"],
        width = 200
    )
    sidebar_label = tk.Label(
        sidebar_frame,
        text = "💰 Finance",
        bg = COLORS["bg_sidebar"],
        fg = COLORS["text_light"],
        font = ("Segoe UI", 16, "bold"),
        pady = 30
    )
    nav_buttons = [
        ("📊 Dashboard",lambda:show_frame(dashboard_frame)),
        ("💸 Transactions",lambda:show_frame(transactions_frame)),
        ("🎯 Budgets",lambda:show_frame(budget_frame)),
        ("📈 Charts",lambda:show_frame(charts_frame)),
        ("🤖 Advisor",lambda:show_frame(advisor_frame))
    ]
    """
    fill="both" — stretches to fill available space in both directions
    fill="y" — stretches vertically only
    expand=True — allows the widget to grow and take extra space
    """
    #pack() method is for placing furniture. Without pack(), widgets don't know where to appear
    content_frame.pack(side="left",fill="both",expand=True)
                       
    dashboard_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    transactions_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    budget_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    charts_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    advisor_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    show_frame(dashboard_frame)

    sidebar_frame.pack(side="right",fill="y")
    sidebar_frame.pack_propagate(False) # this tell the frame to respect the width, not resizing the size based on its content
    sidebar_label.pack(fill="x")
    
    for button, command in nav_buttons:
        btn = tk.Button (  # the tk.Button has default event as "click"
            sidebar_frame,
            text = button,
            command = command,
            bg = COLORS["bg_sidebar"],
            fg = COLORS["text_light"],
            font = ("Segoe UI",11),
            border = 0,
            cursor = "hand2", # this change the pointer cursor into a hand cursor
            anchor = "w", # this control where the text appear in the button, w stand for west, means text appear in the west of the button
            padx = 50,
            pady = 20
        )
        
        btn.pack(fill="x")
        
        btn.bind("<Enter>",lambda e, b=btn: b.config(bg=COLORS["accent"])) # Enter is a event so we have to add <>
        btn.bind("<Leave>",lambda e, b=btn: b.config(bg=COLORS["bg_sidebar"]))
        # explaination for this bind() section is in the document 

    build_transactions_page(transactions_frame,data)
    root.mainloop() 

if __name__ == "__main__":
    main()
    
