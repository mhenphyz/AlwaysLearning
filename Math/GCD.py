# gcd(a, b) = gcd(b, r).

def gcd(a, b):
    
    # make sure that 'a' is the bigger number
    if b > a:
        a, b = b, a

    while True:
        rest = a % b

        if rest == 0:
            return b
        else:
            a = b
            b = rest

        
print(gcd(36,90)) # 18
print(gcd(48,30)) # 6
print(gcd(6,12)) # 6
print(gcd(12,20)) # 4
print(gcd(20,24)) # 4