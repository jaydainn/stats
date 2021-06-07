import numpy as np
from scipy.stats import binom , norm 
import matplotlib.pyplot as plt



size = 10**4
n = 20 
p = 0.3

plt.figure()
plt.title("Loi Binomiale avec numpy")
plt.hist(np.random.binomial(n , p , size) , bins = 60)
plt.show()

plt.figure()
plt.title("Loi binomiale avec numpy")

plt.figure()
plt.title("Loi Normale avec numpy")
plt.hist(np.random.normal(n , p , size) , bins=100)
plt.show()