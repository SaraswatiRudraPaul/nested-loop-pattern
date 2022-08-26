#    *
#   * *
#  * * *
# * * * *
#* * * * *
num=int(input("enter number"))
r=1
while r<=num:
    c=1
    while c<=num-r:
        print(" ",end=" ")
        c=c+1
    k=1
    while k<=r:
        print("*",end=" ")
        k=k+1
        p=0
        while p<1:
            print(" ", end=" ")
            p=p+1
        print( )
    r=r+1