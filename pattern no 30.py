#A
#B C
#D E F
#G H I J
a=int(input("enter number"))
r=65
i=65
while i<=a:
    c=65
    while c<=i:
        print(chr(r),end=" ")
        c=c+1
        r=r+1
    print( )
    i=i+1