marks = {
    "ram": 33,
    "rahul": 45,
    "devesh": 30,
    "jayul": 34,
    "meena": 29,
    "nisha": 37,
    "karan": 40,
    "anita": 18,
    "siddhi": 25
}
sum = 0

for v in marks.items():
    sum = sum + v
    
print("The total marks = ", sum)