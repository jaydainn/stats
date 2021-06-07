import matplotlib.pyplot as plt
import numpy as np 

Nb=[10,20,30,40,50,60,70,80,90,100]
NB2 = [30,40,50,60,70,80]
NB1 =[10,20,30,40,50,60]
NB3 = [40,50,60,70,80,90]
T=[2,4,6,8,10,12,14,16,18,20]
T1=[10,12,14,16,18,20]
Categorie = ["Categorie1", "Categorie2", "Categorie3", "Categorie4"]
Nombre = [5000, 26000, 21400, 12000]

plt.plot(T , Nb)
plt.xlabel("Temps")
plt.ylabel("Pieces Conformes")

fig , axs = plt.subplots(3)
axs[0].plot(T1[:len(NB1)] , NB1 ,  "-r"  )
axs[0].plot(T1[:len(NB2)] , NB2 , "*b"  )
axs[0].plot(T1[:len(NB3)] , NB3 ,"+g" )


axs[0].set_xlabel("Temps")
axs[0].set_ylabel("Pieces Conformes")


axs[1].plot(T1[:len(NB1)] , NB1 ,  "r" , linewidth=7  )
axs[1].plot(T1[:len(NB2)] , NB2 , "b" , linewidth = 12  )
axs[1].plot(T1[:len(NB3)] , NB3 ,"g"  , linewidth=10)


axs[1].set_xlabel("Temps")
axs[1].set_ylabel("Pieces Conformes")

axs[2].pie(Nombre , labels=Categorie)
plt.show()


