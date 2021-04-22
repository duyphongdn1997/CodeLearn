def sequenceNumber(l,r):
    a  = '123456789'
    arr = []
    for i in range(len(str(r))+1):
        if i != 0:
            for v in range(len(a)):
                if int(a[v:v+i]) <= r and int(a[v:v+i]) >= l:
                    arr.append(int(a[v:v+i]))
    return sorted(list(set(arr)))


print(sequenceNumber(100,300))