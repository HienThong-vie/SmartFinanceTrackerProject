from datetime import datetime 
today =  datetime.now()
timeString = today.strftime("%Y-%m-%d")
transactions = [
    {"id":1,
     "time":timeString,
     "amount":300,
     "type": "expense",
     "note": "for buffet night with family",
     "category": "food" },
     {"id":2,
     "time":timeString,
     "amount":150,
     "type": "income",
     "note": "got commission payout",
     "category": "income"}
]