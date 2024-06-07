def is_prime(num):
    count = 0
    res = ""
    for i in range(1,num+1):
        if(num % i == 0):
            count += 1 
    if(count == 2):
        res = "Prime Number"
    else:
        res = "Not a Prime Number"
    return res 
n = int(input())
fin_output = is_prime(n)
print(fin_output)