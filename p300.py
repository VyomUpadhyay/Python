# Her Husband's Expense
his = {
    'Clothes': 1100,
    'Shoes': 1000,
    'Watch': 900,
    'Mobile Recharge': 699,
    'Petrol': 1980
}

# Wife's Expense
wife = {
    'Mobile Recharge': 799,
    'DTH recharge': 999,
    'Clothes': 2310,
    'Makeup': 3670,
    'Shoes': 999
}

# 1. Total expenses for each of his
his_total = sum(his.values())
wife_total = sum(wife.values())

print("Your total expenses:", his_total)
print("Wife's total expenses:", wife_total)

# 2. Who is spending more
if his_total > wife_total:
    print("You are spending more.")
elif wife_total > his_total:
    print("Your wife is spending more.")
else:
    print("Both are spending the same amount.")

# 3. The item his are spending the most on
his_max_item = max(his, key=his.get)
his_max_exp = his[his_max_item]
print("You are spending the most on", his_max_item, ":", his_max_exp)

# 4. The item your wife is spending the most on
wife_max_item = max(wife, key=wife.get)
wife_max_exp = wife[wife_max_item]
print("Your wife is spending the most on", wife_max_item, ":", wife_max_exp)
