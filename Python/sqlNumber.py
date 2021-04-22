def sequenceNumber(l,r):
    sequence = '123456789'
    result = []
    for i in range(len(sequence)+1):
        for v in range(i+1,len(sequence)+1):
            if ((int(sequence[i:v])>l) and int(sequence[i:v]) <r): 
                result.append(int(sequence[i:v]))
    result.sort()
    return result

print(sequenceNumber(100,300))