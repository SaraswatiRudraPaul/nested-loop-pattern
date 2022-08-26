#        1
#      2 1 2
#    3 2 1 2 3
#  4 3 2 1 2 3 4
#5 4 3 2 1 2 3 4 5 
a=int(input("enter number"))
r=1
while r<=a:
    c=1
    while c<=a-r:
        print(" ", end=" ")
        c=c+1
    j=0
    while j<r:
        print(r-j,end="  ")
        j=j+1
    k=2
    while k<=r:
        print(k,end=" ")
        k=k+1
    print( )
    r=r+1