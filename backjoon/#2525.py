#2525
a,b = map(int,input().split())
c=int(input())
c_h=c//60
c_m=c%60
if b+c_m>=60:
    temp_a=a+c_h+1 
    temp_b=b+c_m-60
else:
    temp_a=a+c_h 
    temp_b=b+c_m
if temp_a>=24:
    temp_a-=24
print(temp_a,temp_b)