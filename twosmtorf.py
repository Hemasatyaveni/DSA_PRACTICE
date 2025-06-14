def twosum(arr,target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False
if __name__ == "__main__":
    arr = [1,9,8]
    target=17
    if twosum(arr,target):
        print("true")
    else:
        print("false")
