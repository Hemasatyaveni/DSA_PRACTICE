def container(height):
    n = len(height)
    l = 0
    r = n-1
    max_sum = 0
    while l<r:
        w = r - l
        h = min(height[l],height[r])
        a = w*h
        max_sum = max(max_sum,a)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_sum
height = [1,8,6,2,5,4,8,3,7]
print(container(height))