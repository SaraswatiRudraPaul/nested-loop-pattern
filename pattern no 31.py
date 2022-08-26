#        1
#      2 2 2
#    3 3 3 3 3
#  4 4 4 4 4 4 4
#5 5 5 5 5 5 5 5 5
a=int(input("enter number"))
k=1
i=1
while i<=a:
    c=1
    while c<=5-i:
        print(" ",end=" ")
        c=c+1
    j=1
    while j<=k:
        print(i,end=" ")
        j=j+1
    print( )
    k=k+2
    i=i+1