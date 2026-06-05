d1 = {11: "ram", 13: "mohan", 22: "disha", 35: "neha", 42: "raju", 55: "geeta", 67: "amit", 78: "sita", 89: "kiran", 90: "rohan", 100: "pinki", 112: "arun", 123: "meera", 134: "vijay", 145: "anita", 156: "sumit", 167: "shreya"}

print("The name of failed students are -> ")
for k,v in d1.items():
    if k<70:
        print(v)
print("The name of passes students are -> ")
for k,v in d1.items():
    if k>70:
        print(v)