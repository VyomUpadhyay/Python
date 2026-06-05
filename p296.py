d1={11:[22,33,44],12:[4,5,6]}

for k,v in d1.items():
    m1,m2,m3=v
    total=sum(v)
    print (k,m1,m2,m3,total)
    
    
d1[44]=[11,22,33]

print(d1)