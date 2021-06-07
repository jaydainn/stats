def getIndex(arr , val):
    index = -1
    #parcours la liste et trouve la valeur donné en parametre et retourne son index ou -1 si elle n'existe pas
    for i in range(len(arr)): 
        if(arr[i] == val):
            index = i
    return index


def getOccurences(arr , val):
    #parcours la liste et incremente le nombre d'occurence de la valeur donné
    res = 0
    for i in range(len(arr)):
        if(arr[i] == val):
            res = res +1
    return res


def getSorted(arr):
    # creer une copie de la liste 
    listsorted = arr.copy()
    # trier par ordre croissant
    listsorted.sort()

    # trier par ordre decroissant
    listsortedrev = arr.copy()
    listsortedrev.sort(reverse = True)
    
    
    issorted = True
    issortedreverse =True
    # boucle pour verifier l'ordre de la liste d'origine
    for i in range(len(arr)):
        
        if(arr[i] != listsorted[i] ):
            issorted = False
        if(arr[i] != listsortedrev[i]):
            issortedreverse = False

    res = ""
    #retour en fonction du resultat
    if (issorted and not issortedreverse):
        res += "Trier par ordre croissant"
    if(not issorted and issortedreverse):
        res += "Trier par ordre decroissant"
    if(not issorted and not issortedreverse):
        res += "Non trier"
    return res
        

list = [2 , 4 , 4, 6 , 7 , 8 ]
print("index of 6 : " + str(getIndex(list , 6)))
print("occurences of 4: "+ str(getOccurences(list , 4)))
print(getSorted(list))

