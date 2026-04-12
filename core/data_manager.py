import os 
import json
import uuid
from datetime import datetime
from core.algorithm import merge_sort
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "transactions.json") 
def load_data(): 
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as data_file:
            data = json.load(data_file)   
            return data
    else:
        return {
            "transactions": [],
            "budgets": {},
            "categories": [
        "food",
        "rent",
        "transport",
        "shopping",
        "supplement",
        "drinks"
        ]
    }

def save_data(data):
    with open(DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4) 


def add_transaction(data,amount,transaction_type,category,note):
    transaction_id = str(uuid.uuid4())

    new_transaction = {
        "id":transaction_id,
        "time":datetime.now().strftime("%Y-%m-%d"),
        "amount":amount,
        "type": transaction_type,
        "note": note,
        "category": category
    }
    data["transactions"].append(new_transaction)
    save_data(data)

def delete_transaction(transaction_id, data):
    for transaction in data["transactions"]:
        if transaction_id == transaction["id"]:
            data["transactions"].remove(transaction)
            save_data(data)
            break

def edit_transaction(data,transaction_id,updated_field):
    matching_transaction = None
    for transaction in data["transactions"]:
        if transaction_id == transaction["id"]:
            matching_transaction = transaction
            break 
    if matching_transaction is not None: 
            matching_transaction.update(updated_field)
            save_data(data)


def get_transaction(data,search_query=None,sort_by="time",ascending=False):
    transactions =  data["transactions"]
    if search_query is not None:
        search_query = search_query.lower()
        transactions = [
            transaction for transaction in transactions 
                if search_query in transaction["time"].lower()
                or search_query in transaction["note"].lower()
                or search_query in transaction["type"].lower()
                or search_query in transaction["category"].lower()
                or search_query in str(transaction["amount"])
            ]
    transactions = merge_sort(transactions,sort_by, reverse= not ascending)
    return


def add_budget(data,category,limit,period):
    category = category.lower()
    data["budgets"][category] = {"limit": limit,"period": period,"start_date":datetime.now().strftime("%Y-%m-%d")}
    save_data(data)

def delete_budget(data,category):
    category = category.lower()
    if category in data["budgets"]:
        del data["budgets"][category]
        save_data(data)

def get_budget(data):
    return data["budgets"]

def add_category(data,category):
    category = category.lower()
    if category in data["categories"]:
        return
    else:
        data["categories"].append(category)
        save_data(data)

def get_categories(data):
    return data["categories"]

def remove_category(data,category):
    if category in data["categories"]:
        data["categories"].remove(category)
        save_data(data)
        