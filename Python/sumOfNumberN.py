creat_number = lambda n : (2*n - 1)*(2*n - 1)*(2*n - 1)

stored_results = {}
def sum_of_cubes_odd_numbers(n):

    result = 0
    for i in reversed(range(n)):
        print("i = {} \t n(i) = {}".format(i+1,creat_number(i+1)) )
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            print("result = ",result)
            break
        else:
            result += creat_number(i + 1)
            print("result = ",result)
    stored_results[n] = result
    return result

n = 7
print(sum_of_cubes_odd_numbers(n))
