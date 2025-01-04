#10818
n=int(input())
l=[int(num) for num in input().split()]
l.sort()
print(f"{l[0]} {l[-1]}")
