a = 24
b = 36 
LCM = b
while (LCM%a!=0) or (LCM%b != 0):
    if (a < b): LCM+=a
    else: LCM+=b
print(LCM)

