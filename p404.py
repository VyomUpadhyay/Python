from pymongo import MongoClient
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["movie"]

def insert_movie():
    """Insert a new movie into the collection."""
    mname = input("Enter Movie Name: ")
    hero = input("Enter Hero Name: ")
    ryear = int(input("Enter Release Year: "))
    income = int(input("Enter Income: "))
    budget = int(input("Enter Budget: "))

    movie = {
        "MNAME": mname,
        "HERO": hero,
        "RYEAR": ryear,
        "INCOME": income,
        "BUDGET": budget
    }

    collection.insert_one(movie)
    print("✅ Movie inserted successfully!")

def display_movies():
    """Display all movies with formatting and color."""
    all_movies = collection.find()
    print("\n🎬 All Movies:\n")

    header = f"{'MOVIE':<20}{'HERO':<15}{'YEAR':<8}{'INCOME':<10}{'BUDGET':<10}"
    print(Style.BRIGHT + header + Style.NORMAL)

    for e1 in all_movies:
        mname = e1["MNAME"].upper()
        hero = e1["HERO"].capitalize()
        ryear = e1["RYEAR"]
        income = e1["INCOME"]
        budget = e1["BUDGET"]

        color = Fore.GREEN if income > budget else Fore.RED

        line = (
            color +
            Style.BRIGHT + f"{mname:<20}" +
            Style.NORMAL + f"{hero:<15}{ryear:<8}{income:<10}{budget:<10}"
        )
        print(line)

# First, insert a movie
insert_movie()

# Then, display all movies
display_movies()
