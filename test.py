import tkinter as tk 
test_list = [1,2,3]
mutiply_by_two = [n for n in test_list]

print(mutiply_by_two)
#test list comprehension concepts
budgets = {
    "Food" : {"limit": 300,"period": "week","start_date": "today" },
    "GymMembership" : {"limit": 150, "period": "month","start_date": "today"},
    "Gas" : {"limit": 100, "period":  "week","start_date": "today"}
}         
for budget in budgets:
    print(budgets[budget]["limit"])
    
list_1 = ["noname1","noname2","noname3"]
list_2 = ["name1","name2","name3"]

