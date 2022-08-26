#A
#A B 
#A B C 
#A B C D
#A B C D E
a=int(input("enter number"))
r=65
while r<=a:
    c=65
    while c<=r:
        print(chr(c),end=" ")
        c=c+1
    print( )
    r=r+1