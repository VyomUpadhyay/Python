import time
from colorama import Fore

turn = 1
list1 = ['_','_','_','_','_','_','_','_','_']
Name1 = str(input("Enter the name of Player 1 -> "))
Name2 = str(input("Enter the name of Player 2 -> "))

starting_time = time.time()

while turn < 10:

    if turn % 2 == 0:
        time.sleep(0.7)
        print(Fore.RED, Name1, " your turn")
        position = int(input(" Enter the position !! -> "))
        list1[position-1] = 'X'
    else:
        time.sleep(0.7)
        print(Fore.BLUE, Name2, " your turn")
        position = int(input(" Enter the position !! -> "))
        list1[position - 1] = '0'

    print(" After ", turn)
    print("  ", list1[0], " | ", list1[1], " | ", list1[2])
    print("  ", list1[3], " | ", list1[4], " | ", list1[5])
    print("  ", list1[6], " | ", list1[7], " | ", list1[8])
    turn += 1

    if list1[0] == list1[1] and list1[0] == list1[2]:
        if list1[0] == "0":
            print(Name2, "is winner")
            break
        elif list1[0] == "X":
            print(Name1, "is winner")
            break
    if list1[3] == list1[4] and list1[3] == list1[5]:
        if list1[3] == "0":
            print(Name2, "is winner")
            break
        elif list1[3] == "X":
            print(Name1, "is winner")
            break
    if list1[6] == list1[7] and list1[6] == list1[8]:
        if list1[6] == "0":
            print(Name2, "is winner")
            break
        elif list1[6] == "X":
            print(Name1, "is winner")
            break
    if list1[0] == list1[3] and list1[0] == list1[6]:
        if list1[0] == "0":
            print(Name2, "is winner")
            break
        elif list1[0] == "X":
            print(Name1, "is winner")
            break
    if list1[1] == list1[4] and list1[1] == list1[7]:
        if list1[1] == "0":
            print(Name2, "is winner")
            break
        elif list1[1] == "X":
            print(Name1, "is winner")
            break
    if list1[2] == list1[5] and list1[2] == list1[8]:
        if list1[2] == "0":
            print(Name2, "is winner")
            break
        elif list1[2] == "X":
            print(Name1, "is winner")
            break
    if list1[0] == list1[4] and list1[0] == list1[8]:
        if list1[0] == "0":
            print(Name2, "is winner")
            break
        elif list1[0] == "X":
            print(Name1, "is winner")
            break
    if list1[2] == list1[4] and list1[2] == list1[6]:
        if list1[2] == "0":
            print(Name2, "is winner")
            break
        elif list1[2] == "X":
            print(Name1, "is winner")
            break

    if turn == 10:
        print("The game is tie")

ending_time = time.time()
total_time = ending_time - starting_time
print("\nGame finished in", round(total_time, 2), "seconds ⏱️")
