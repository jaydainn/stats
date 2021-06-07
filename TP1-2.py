def createList(n):
    ls = []
    for i in range(n):
        ls.append(int(input("valeur index "+ str(i) + ": \n" )))
    return ls

def getMean(arr):
    valpos = 0
    valneg = 0 
    respos = 0 
    resneg = 0 
    for i in range(len(arr)):
        if(arr[i] > 0):
            valpos = valpos + 1 
            respos = respos + arr[i] 
        else : 
            valneg = valneg + 1 
            resneg = resneg + arr[i]
    print((respos/valpos))
    print((resneg/valneg))


print(getMean(createList(5)))


