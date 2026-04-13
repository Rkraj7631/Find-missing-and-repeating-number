def miss_repeat(arr):
    n=len(arr)

    s=n*(n+1)//2
    p=n*(n+1)*(2*n+1)//6

    ac_sum=sum(arr)
    sq_sum=sum(x*x for x in arr)

    diff=s-ac_sum
    sq_diff=p-sq_sum

    sum_xy=sq_diff//diff

    x=(diff+sum_xy)//2
    y=x-diff

    return x,y

arr = [1, 2, 2, 4, 5]
missing, repeating = miss_repeat(arr)

print(f"Missing : ", missing)
print(f"Repeating :", repeating)
