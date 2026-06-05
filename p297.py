
cp = {
    "china": 143,
    "india": 136,
    "usa": 32,
    "uk": 21
}


while True:
    print("\nChoose an option:")
    print("1. Print all countries with their population")
    print("2. Add a new country and its population")
    print("3. Remove a country")
    print("4. Query the population of a country")
    print("5. Exit the program")

    option = input("Enter your option (1-5): ")

    if option == "1":

        for country, population in cp.items():
            print(country + "==>" + str(population))

    elif option == "2":

        cn = input("Enter the country name to add: ").lower()
        if cn in cp:
            print(cn + " already exists!")
        else:
            population = int(input("Enter the population of " + cn + ": "))
            cp[cn] = population
            print(cn + "==>" + str(population))

    elif option == "3":

        cn = input("Enter the country name to remove: ").lower()
        if cn in cp:
            del cp[cn]
            for country, population in cp.items():
                print(country + "==>" + str(population))
        else:
            print(cn + " doesn't exist!")

    elif option == "4":
       
        cn = input("Enter the country name to query: ").lower()
        if cn in cp:
            print("The population of " + cn + " is " + str(cp[cn]))
        else:
            print(cn + " doesn't exist!")

    elif option == "5":
       
        print("Exiting the program.")
        break   

    else:
       
        print("Invalid option. Please try again.")