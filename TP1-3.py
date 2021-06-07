
def crossProduct(arr1 , arr2):
    #fonction permettant de calculer le produit vectoriel de deux vecteur en utilisant l'algorithme de sarus
    res = [] 
    for i in range(len(arr2)):
        res.append(0)
  
    for i in range(len(arr2)):
        res [i] = arr1[(i+1) % len(arr1)] * arr2[(i+2) % len(arr1)] - arr1[(i+2) % len(arr1)] * arr2[(i+1) % len(arr1)]
    return res

def dotProduct(arr1 , arr2):
    #parcours les liste et effectue la somme des xi*yi pour trouver le produit scalaire
    res = 0 
    for i in range(len(arr1)):
        res = res + (arr1[i] * arr2[i])
    return res 

def vectorModule(arr1):
    #parcours une liste et ajoute a une variable la somme des carré des xi
    res = 0 
    for i in range(len(arr1)):
        res = res + arr1[i] * arr1[i]
    #retourne la racine carré de cette somme sans utilisé de librairie externe 
    return res**(1/2)


def vectorsDef(arr1 , arr2):
    #utilise les fonctions definies precedemment pour caracteriser deux vecteurs
    res = "Quelconques"
    if(dotProduct(arr1 , arr2) == 0 ):
        res = "Orthogonaux"
    if(dotProduct(arr1 , arr2) == vectorModule(arr1) * vectorModule(arr2)):
        res = "colineaires"
    return res
        
a = [2 , 0]
b = [0 , 2]


print(crossProduct(a , b))
print(dotProduct(a , b))
print(vectorsDef(a , b))

