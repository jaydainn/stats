import numpy as np

def getMoyenne(arr):
    s = 0 ;
    for i in range(len(arr)):
        s+= arr[i]
    return s/len(arr)


def getMoyenneNumpy(arr):
    return np.mean(arr)


def getVariance(arr):
    s = 0 ; 
    for i in range(len(arr)):
        s += arr[i] ** 2
    return ((1/len(arr)) * s ) - getMoyenne(arr)**2

def getVariance2(arr):
    s = 0 ; 
    for i in range(len(arr)):
        s += (arr[i] - getMoyenne(arr)) ** 2
    return s/len(arr)


def getVarianceLib(arr):
    return np.var(arr)

list = [1 , 2 ,3 , 5]

print("Moyenne sans librairie: " + str(getMoyenne(list)))
print("Moyenne avec np.mean: " + str(getMoyenneNumpy(list)))
print("Variance avec la premiere formule: " + str(getVariance(list)))
print("Variance avec la deuxieme formule: "+ str(getVariance2(list)))
print("Variance avec np.var: "+ str(getVarianceLib(list)))

