import time
def to_digit(n):
    n = str(n)
    result = []
    for i in n:
        result.append(int(i))
    return result

def to_number(arr):
    result = 0
    for i in range(len(arr)) :
        result += arr[i]*pow(10,len(arr)-i-1)
    return result

def min_max(n):
    arr = to_digit(n)
    print(arr)
    arr1 = to_number(sorted(arr))
    arr2 = to_number(sorted(arr, reverse=True))
    
    print("arr 1 = {} \t arr 2 = {}".format(arr1, arr2))
    return arr2 - arr1 

t = time
print(min_max(312))
print(time.time() - t)