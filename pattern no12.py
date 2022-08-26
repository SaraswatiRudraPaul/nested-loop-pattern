#1
#2 3
#4 5 6 
#7 8 9 10
a=int(input("enter number"))
r=1
b=1
while r<=a:
    c=1
    while c<=r:
        c=c+1
    k=1
    while k<=r:
        print(b,end=" ")
        b=b+1
        k=k+1
    print( )
    r=r+1