def uniqueNumber(arr):
    for i in reversed(range(len(arr))):
        print("i = {} arr.index({}) = {}".format(i,i,arr.index(arr[i])) )
        # if arr.index(i) == i : 
        #     return arr[i]
    return -1

print(uniqueNumber([19, 17, 19, 68, 68]))