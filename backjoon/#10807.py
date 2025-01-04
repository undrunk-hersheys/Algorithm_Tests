#10807
n=int(input())
l=[int(num) for num in input().split()]
v=int(input())
count=0
for i in l:
    if v==i:
        count+=1
print(count)