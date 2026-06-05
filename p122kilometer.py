for i in range(1, 6):

    tired = input("Are you tired ?? ").lower()

    if tired=="yes":
        print("You didn't finish the race...")
        print("You ran ", i ,"kilometers")
        break
if i==5:
    print("Congratulations.. you have completed the race")