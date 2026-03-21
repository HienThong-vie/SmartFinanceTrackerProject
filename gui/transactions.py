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

    def delete_fields():
        amount_entry.delete(0,tk.END)
        category_combobox.set("") # to delete combobox, we use set() with an empty string
        type_combobox.set("")
        note_entry.delete(0,tk.END)

    # widgets section
    form_frame = tk.LabelFrame(
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
    # pack section
    form_frame.pack(fill="x", padx=20, pady=10)

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
    