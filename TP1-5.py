val = int(input("choisir un nombre: "))
#demande a l'utilisateur de choisir un nombre
res = ""
for i in range(1 , val +1):
    #ajoute i a un string de resultat pour donner l'affichage attendu 
    res += " " + str(i)
    print(res)
