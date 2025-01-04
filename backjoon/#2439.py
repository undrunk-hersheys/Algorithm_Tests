#2439
n=int(input())
for i in range(1,n+1):
    for ii in range(n-i):
        print(" ",end='')
    for iii in range(i):
        print("*",end='')
    print("")