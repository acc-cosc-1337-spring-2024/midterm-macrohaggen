def is_prime(num):
    if num<2:
        return False
    else:
        for int in range(2, num//2+1):
            if(num%int==0):
                return False
        return True
none = 1
while none==1:
    numbo = int(input("Input Number:\n"))
    print(is_prime(numbo))
    if str(input("end? (y/n)\n"))=="y":
        none = 0
    else:
        continue