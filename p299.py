exp = {
    'January': 2200,
    
    'February': 2350,
    
    'March': 2600,
    
    'April': 2130,
    
    'May': 2190,
    
    'June': 1980,
    
    'July': 2400,
    
    'August': 2250,
    
    'September': 2100,
    
    'October': 2400,
    
    'November': 2150,
    
    'December': 2500
}

# 1. Extra spent in February compared to January
extra = exp['February'] - exp['January']
print("Extra in February:", extra)


# 2. Total expenses for the first quarter (Jan to Mar)
total_q1 = exp['January'] + exp['February'] + exp['March']
print("Total Q1 expenses:", total_q1)


# 3. Check if 2400 was spent in any month
spent_2400 = [month for month, amount in exp.items() if amount == 2400]
print("Months with 2400 spent:", spent_2400)


# 4. Modify June expense to 2080
exp['June'] = 2080
print("Updated June expense:", exp['June'])


# 5. Refund of 200 in April
exp['April'] -= 200
print("Updated April expense after refund:", exp['April'])


# 6. Find the month with the highest expense
max_month = max(exp, key=exp.get)
max_exp = exp[max_month]
print("Month with highest expense:", max_month, max_exp)


# 7. Average expense for the first half of the year (Jan to Jun)
avg_half = sum([exp[m] for m in ['January', 'February', 'March', 'April', 'May', 'June']]) / 6
print("Average expense for first half:", avg_half)


# 8. Find the month with the lowest expense
min_month = min(exp, key=exp.get)
min_exp = exp[min_month]
print("Month with lowest expense:", min_month, min_exp)
