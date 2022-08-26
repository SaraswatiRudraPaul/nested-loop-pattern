#        1
#      2 1
#    3 2 1
#  4 3 2 1
#5 4 3 2 1
a=int(input("enter number"))
r=0
while r<=a:
    c=a-r
    while c>0:
        print(" ",end=" ")
        c=c-1
    n=r+1
    while n>0:
        print(n,end=" ")
        n=n-1
    print( )
    r=r+1