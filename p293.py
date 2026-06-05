marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25
}

passed_students = sum(1 for mark in marks.values() if mark >= 18)

print(f"Number of passed students: {passed_students}")
