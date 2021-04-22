def check_special_number(n):
    n = str(n)
    for i in range(len(n)):
        if (n.find(n[i]) != i) : return False
            
    
    return True

n = 123
print(check_special_number(n))
n = 113
print(check_special_number(n))