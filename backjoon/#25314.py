#25314
N=int(input())
i=N//4
if N%4!=0:
    i+=1
for ii in range(i):
    print("long ",end='')
print("int")