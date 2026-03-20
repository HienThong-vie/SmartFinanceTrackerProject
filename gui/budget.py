from datetime import datetime
today = datetime.now()
timeString = today.strftime("%Y-%m-%d")
budgets = {
    "Food" : {"limit": 300,"period": "week","start_date": timeString },
    "GymMembership" : {"limit": 150, "period": "month","start_date": timeString},
    "Gas" : {"limit": 100, "period":  "week","start_date": timeString}
}
# we will need to update the date later to calculate when the week reset