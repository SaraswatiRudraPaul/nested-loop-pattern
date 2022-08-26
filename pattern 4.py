#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=5-r+1:
        print(c,end=" ")
        c=c+1
    print( )
    r=r+1