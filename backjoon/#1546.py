#1546
n=int(input())
l=[int(num) for num in input().split()]
l.sort()
temp=0
for i in l:
    temp+=i/l[-1]*100
print(temp/n)