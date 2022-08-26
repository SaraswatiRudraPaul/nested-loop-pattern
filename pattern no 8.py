#        1
#      1 2
#    1 2 3
#  1 2 3 4
#1 2 3 4 5
a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=a-r:
        print(" ",end=" ")
        c=c+1
    k=1
    while k<=r:
        print(k,end=" ")
        k=k+1
    print( )
    r=r+1