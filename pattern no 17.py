#1
#3 3 
#5 5 5
#7 7 7 7
#9 9 9 9 9
a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=r:
        print(r*2-1,end=" ")
        c+=1
    print( )
    r+=1