#A
#B B
#C C C
#D D D D
#E E E E E
a=int(input("enter number"))
r=65
while r<=a:
    c=65
    while c<=r:
        print(chr(r),end=" ")
        c=c+1
    print( )
    r=r+1