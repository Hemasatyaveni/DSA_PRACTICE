def minimumsum (arr):
    total = sum(arr)
    freq = { }
    for num in arr:
        freq[num] = freq.get(num,0)+1
    minsum = float('inf')
    for num in freq:
        currentval = total - (num*freq[num])
        minsum = min(minsum,currentval)
    return minsum
arr = [5,4,6,6]
print(minimumsum(arr))
