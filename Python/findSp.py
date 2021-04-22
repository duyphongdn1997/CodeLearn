def findSpecialNumber(n):
    arr = [1, 2, 2]
    try:
        return arr[n-1]
    except IndexError:
        i = 3
        while True:
            arr += [i]*arr[i-1]
            print(arr)
            if n <= len(arr):
                return arr[-1]
            i += 1

n = 15
print(findSpecialNumber(n))