#2480
def dice(dice_list):
    dice_list.sort()
    if dice_list[0]==dice_list[1]==dice_list[2]:
        prize=10000+1000*dice_list[-1]
    elif dice_list[0]==dice_list[1] or dice_list[1]==dice_list[2]:
        prize=1000+100*dice_list[-2]
    else:
        prize=100*dice_list[-1]
    return prize 

# a,b,c=map(int,input().split())
dice_list=list(map(int,input().split()))
p=dice(dice_list)
print(p)