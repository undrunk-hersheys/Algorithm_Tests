#10871
n, x= map(int,input().split())
l=[int(num) for num in input().split()]
temp=[]
for i in l:
    if i<x:
        print(i, end=' ')
print()
