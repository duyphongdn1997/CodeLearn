def fibonacci_iterative(n):
    arr = [0,1,1]
    if n<2 : return arr[n]
    a,b = 2,3
    for i in range(2,n+1):
        arr.append(a) 
        b = b + a
        a = b - a
    return arr[n]

if __name__ == "__main__" :
    print(fibonacci_iterative(10))