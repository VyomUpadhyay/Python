Number = int(input("Enter limit =>"))
s=0
for i in range(1, Number+1):
    if i==Number:
        print(i*i*i,end="  " )
    else:
        print(i*i*i,end=" + " )
    s=s+i*i*i
print("\nSum = ",s)

