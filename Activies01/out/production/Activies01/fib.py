def fibonacci_iterative(n):
    arr = list((0, 1, 1))
    # arr[0] = 0
    # arr[1] = 1
    # arr[2] = 1
    if n < 2:
        return arr[n]
    a, b = 2, 3
    for i in range(3, n):
        arr.append(a)
        b = b + a
        a = b - a
    return arr[n]


if __name__ == '__main__':
    print(fibonacci_iterative(5))
