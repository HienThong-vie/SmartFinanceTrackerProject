import tkinter as tk
import tkinter.ttk as ttk
from constants import COLORS
from datetime import datetime
from core.data_manager import (
    get_transaction,
    add_transaction,
    edit_transaction,
    delete_transaction,
    get_categories,
    add_category,
    save_data
)
def build_transactions_page(frame, data):
    def refresh_table():
        transaction_history.delete(*transaction_history.get_children()) # this delete all children widget (columns) inside a tree widget
        transactions = get_transaction(data) # we need to loop through this dict to find all transaction category
        for transaction in transactions:
            transaction_history.insert("",tk.END,values=(
                transaction["time"],
                transaction["type"],
                transaction["category"],
                transaction["amount"],
                transaction["note"]
            ))

    def submit_transaction():
        try: # we try the input to make sure it is an integer first
            amount = int(float(amount_entry.get()))
        except: # if not integer, return imidiatly without crashing
            return 
        category = category_combobox.get()
        transaction_type = type_combobox.get()
        note = note_entry.get()

        add_transaction(data,amount,transaction_type,category,note)

        delete_fields()
        refresh_table()

    def delete_fields():
        amount_entry.delete(0,tk.END)
        category_combobox.set("") # to delete combobox, we use set() with an empty string
        type_combobox.set("")
        note_entry.delete(0,tk.END)

    # widgets section
    form_frame = tk.LabelFrame( # LabelFrame create a form with visible border
        frame,
        text="ADD TRANSACTION",
        bg=COLORS["bg_main"],
        fg=COLORS["text_secondary"],
        font=("Segoe UI", 10, "bold"),
        padx=15,
        pady=10,   
    )
    amount_label = tk.Label(
        form_frame,
        text = "Amount:",
        bg=COLORS["bg_main"],
        fg=COLORS["text_primary"],
        font=("Segoe UI", 10)  
    )
    amount_entry = tk.Entry(
        form_frame,
    )
    category_label = tk.Label(
        form_frame,
        text = "Category",
        bg=COLORS["bg_main"],
        fg=COLORS["text_primary"],
        font=("Segoe UI", 10)        
    )
    # combox is just basically a drop down input
    category_combobox = ttk.Combobox(
        form_frame,
        values=get_categories(data),
        state="readonly"
    )
    type_label = tk.Label(
        form_frame,
        text = "Type",
        bg=COLORS["bg_main"],
        fg=COLORS["text_primary"],
        font=("Segoe UI", 10)
    )
    type_combobox = ttk.Combobox(
        form_frame,
        values = ["expense","income"],
        state="readonly"
    )
    date_label = tk.Label(
        form_frame,
        text = "Date:",
        bg=COLORS["bg_main"],
        fg=COLORS["text_primary"],
        font=("Segoe UI", 10)
    )
    date_entry = tk.Entry(
        form_frame
    )
    date_entry.insert(0,datetime.now().strftime("%Y-%m-%d"))
    note_label = tk.Label(
        form_frame,
        text = "Note (Optional)",
        bg=COLORS["bg_main"],
        fg=COLORS["text_primary"],
        font=("Segoe UI", 10)
    )
    note_entry = tk.Entry(
        form_frame,
    )
    sumit_button = tk.Button(
        form_frame,
        command=submit_transaction,
        text="➕ Add Transaction",
        bg=COLORS["accent"],
        fg=COLORS["text_light"],
        font=("Segoe UI", 10, "bold"),
        border=0,
        cursor="hand2"
    )
    """done transaction section"""
    history_frame = tk.LabelFrame(
        frame,
        text="TRANSACTION HISTORY",
        bg=COLORS["bg_main"],
        fg=COLORS["text_secondary"],
        font=("Segoe UI", 10, "bold"),
    )
    transaction_history = ttk.Treeview (
        history_frame,
        columns = ("date","type","category","amount","note"),
        show="headings"
    )
    transaction_history_scrollbar = ttk.Scrollbar(
        history_frame,
        command=transaction_history.yview,
        orient="vertical"
    )
    #ttk widget need style() to styling them
    style = ttk.Style()
    style.configure("Treeview",rowheight=50,font=("Segoe UI", 10))
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
    transaction_history.configure(yscrollcommand=transaction_history_scrollbar.set)
    # define column heading
    transaction_history.heading("date", text="Date")
    transaction_history.heading("type", text="Type")
    transaction_history.heading("category", text="Category")
    transaction_history.heading("amount", text="Amount")
    transaction_history.heading("note", text="Note")
    # defind column width
    transaction_history.column("date", width=90,minwidth=80, anchor="center")
    transaction_history.column("type", width=80,minwidth=70, anchor="center")
    transaction_history.column("category", width=90,minwidth=80, anchor="center")
    transaction_history.column("amount", width=80,minwidth=70, anchor="center")
    transaction_history.column("note", width=150,minwidth=100, anchor="w",stretch=tk.YES)
    # insert a row 
    # transaction frame section
    form_frame.pack(fill="x", padx=20, pady=10) # we dont add fill both here because this frame have fixed height created by all the widget inside this frame

    amount_label.grid(row=0, column=0, sticky="w",pady=5)
    amount_entry.grid(row=0, column=1, sticky="ew",padx=20,pady=5)

    category_label.grid(row=1, column=0, sticky="w",pady=5)
    category_combobox.grid(row=1, column=1, sticky="ew",padx=20,pady=5)

    type_label.grid(row=2, column=0, sticky="w",pady=5)
    type_combobox.grid(row=2, column=1, sticky="ew",padx=20,pady=5)

    date_label.grid(row=3, column=0, sticky="w",pady=5)
    date_entry.grid(row=3, column=1, sticky="ew",padx=20,pady=5)

    note_label.grid(row=4, column=0, sticky="w",pady=5)
    note_entry.grid(row=4, column=1, sticky="ew",padx=20,pady=5)

    sumit_button.grid(row=5, column=1,sticky="e",pady=10)

    form_frame.columnconfigure(1, weight=1)
    # history frame section
    history_frame.pack(fill="both",expand=True,padx=20,pady=10)
    transaction_history_scrollbar.pack(side="right", fill="y")# we need to fill both because this frame will take all the remaining page of screen, leaving no blank space
    transaction_history.pack(fill="both",expand=True,padx=10,pady=10)

    refresh_table()
    
