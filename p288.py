marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}

print(f"{'name':<10}{'mark':<7}{'result'}")

for student, mark in marks.items():
    result = "pass" if mark >= 18 else "fail"
    print(f"{student:<10}{mark:<7}{result}")
