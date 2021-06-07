import numpy as np
from scipy.stats import binom , norm 
import matplotlib.pyplot as plt



size = 10**4
n = 20 
p = 0.3

plt.figure()
plt.title("Loi Binomiale avec numpy")
plt.hist(np.random.binomial(n , p , size) , bins = 60)


plt.figure()
plt.title("Loi binomiale avec scipy")
xval = np.arange(0 ,20 ,  1)
plt.stem(xval , binom.pmf(xval ,  20 , 0.3) , )


plt.figure()
plt.title("Loi Normale avec numpy")
plt.hist(np.random.normal(n , p , size) , bins=100)
plt.show()

plt.figure()
plt.title("Loi Normale avec scipy")
xval = np.arange(0,20,0.01)
plt.plot(xval , norm.pdf(xval , 20/2 , 0.3))
plt.show()