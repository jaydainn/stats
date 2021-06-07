def fact(n):
    if(n == 1):
        return 1
    else:
        return n * fact(n-1)


print(fact(5))

def kinn(k , n):
    return (fact(n)/(fact(k)  * fact(n-k)))

print(kinn(2,3))