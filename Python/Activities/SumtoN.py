import time

stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result

if __name__ == '__main__':
    arr = [1, 2, 3 ,4, 5]
    results = list()
    add = lambda x, y : x + y
    for i in range(len(arr)-1) :
        results.append(add(arr[i],arr[i+1]))
    print(results)
    arr.insert(0,0)