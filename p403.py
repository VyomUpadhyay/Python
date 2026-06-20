from pymongo import MongoClient
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["movie"]

all_myemployees = collection.find()
print("All Movies:\n")

# Optional: Table Header
header = f"{'MOVIE':<20}{'HERO':<15}{'YEAR':<8}{'INCOME':<10}{'BUDGET':<10}"
print(Style.BRIGHT + header + Style.NORMAL)

# Loop through movie documents
for e1 in all_myemployees:
    mname = e1["MNAME"].upper()
    hero = e1["HERO"].capitalize()  # Sentence case
    ryear = e1["RYEAR"]
    income = e1["INCOME"]
    budget = e1["BUDGET"]

    # Color for Hit/Flop
    color = Fore.GREEN if income > budget else Fore.RED

    # Format and print each row
    line = (
        color +
        Style.BRIGHT + f"{mname:<20}" +  # Movie name bold and upper
        Style.NORMAL + f"{hero:<15}{str(ryear):<8}{str(income):<10}{str(budget):<10}"
    )
    print(line)
