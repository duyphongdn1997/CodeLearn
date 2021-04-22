def plantFlowers(arr,n):
    count = 0
    arr = [0] + arr + [0]
    print (arr)
    i = 0

    for i in range (1,len(arr)-1):
        print(i)
        if arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0 :
            count += 1
            arr[i] = 1
            print(i)
            print(arr)        

    print("count = ",count)
    if count >= n : 
        return True, arr
    else : 
        return False, arr

def diff (arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] -= arr2[i]
    return arr1


arr_origin = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
arr = arr_origin
n = 1
check, arr = plantFlowers(arr, n)
print(check)
# print(diff(arr,arr_origin))