
turn=1
list1=['_','_','_','_','_','_','_','_','_']
while turn<10:

    if turn%2 ==0:
        position = int(input("Enter the position Om!! -> "))
        list1[position-1]='X'
    else:
        position = int(input("Enter the position Rehaan!! -> "))
        list1[position - 1] = '0'

    print("After ",turn)
    print(list1[0]," | ",list1[1]," | ",list1[2])
    print(list1[3]," | ",list1[4]," | ",list1[5])
    print(list1[6]," | ",list1[7]," | ",list1[8])
    turn=turn+1

    if list1[position%4==0] and 'X':
        print("X won the game")
    elif list1[position%3==0] and 'X':
        print("X won the game")
    elif list1[position%2==0] and 'X':
        print("X won the game")
    elif list1[position+1] and 'X':
        print("X won the game")
    elif list1[1] and list1[4] and list1[2] and 'X':
        print("X won the game")
    elif list1[2] and list1[5] and list1[8] and 'X':
        print("X won the game")
    else:
        print()