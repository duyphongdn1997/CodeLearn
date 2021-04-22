pointAtN = lambda n : 5*(n-1) - (2*(n-2)+1)

def countPoints2(n):
    if n == 0 : return 0
    if n == 1 : return 0
    result = 5
    for i in range(3,n+1):
        # if i == 0 : continue
        # if i == 1 : continue
        result += pointAtN(i)
        print("point at {} = {}".format(i, pointAtN(i)))
        print("result = ", result)
    return result

print(countPoints2(7))