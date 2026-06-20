from pymongo import MongoClient
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]  # Use your actual database name here
collection = db["movie"]  # Collection with movie data

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
    """Display all movies in the collection with colors and formatting."""
    all_movies = collection.find()
    print("\n🎬 All Movies:\n")

    header = f"{'MOVIE':<20}{'HERO':<15}{'YEAR':<8}{'INCOME':<10}{'BUDGET':<10}"
    print(Style.BRIGHT + header + Style.NORMAL)

    for e1 in all_movies:
        mname = e1["MNAME"].upper()  # Uppercase and bold
        hero = e1["HERO"].capitalize()  # Sentence case
        ryear = e1["RYEAR"]
        income = e1["INCOME"]
        budget = e1["BUDGET"]

        # Hit or Flop coloring
        color = Fore.GREEN if income > budget else Fore.RED

        line = (
            color +
            Style.BRIGHT + f"{mname:<20}" +  # Bold Movie name
            Style.NORMAL + f"{hero:<15}{ryear:<8}{income:<10}{budget:<10}"
        )
        print(line)

def update_movie():
    """Update a movie's details."""
    mname = input("Enter Movie Name to update: ").strip()
    field = input("Enter field to update (HERO, RYEAR, INCOME, BUDGET): ").strip().upper()
    new_value = input(f"Enter new value for {field}: ").strip()

    if field in ["RYEAR", "INCOME", "BUDGET"]:
        new_value = int(new_value)

    result = collection.update_one(
        {"MNAME": mname},
        {"$set": {field: new_value}}
    )

    if result.matched_count > 0:
        print("✅ Movie updated successfully!")
    else:
        print("❌ Movie not found.")

def delete_movie():
    """Delete a movie from the collection."""
    mname = input("Enter Movie Name to delete: ").strip()
    result = collection.delete_one({"MNAME": mname})

    if result.deleted_count > 0:
        print("🗑️ Movie deleted successfully!")
    else:
        print("❌ Movie not found.")

def main():
    """Menu-driven program for managing movies."""
    while True:
        print("\n📽️ Menu:")
        print("1. Insert Movie")
        print("2. Display All Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            insert_movie()
        elif choice == "2":
            display_movies()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()