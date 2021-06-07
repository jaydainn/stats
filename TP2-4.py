import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import binom , norm


std = 2
mean = 0
xval = np.arange(-5 , 5 , 0.1);

fig , axs  = plt.subplots(3 , 3 )

axs[0][0].set_title("Loi Gaussienne")
axs[0][0].plot(xval , norm.pdf(xval, mean , std))
std = 1 
axs[0][0].plot(xval , norm.pdf(xval, mean , std))
std = 0.5
axs[0][0].plot(xval , norm.pdf(xval, mean , std))


axs[1][0].set_title("Loi de cauchy")
cauchy = np.random.standard_cauchy(1000)
axs[1][0].hist(cauchy[(cauchy > -5) & (cauchy < 5)] , bins=100)

axs[1][1].set_title("Loi de  Gamma")

k = 0.5
p2 = 1 

axs[1][1].hist(np.random.gamma(k , p2 , 1000) , bins=100)
k = 1 
axs[1][2].hist(np.random.gamma(k , p2 , 1000) , bins=100)
k = 2
axs[2][0].hist(np.random.gamma(k , p2 , 1000) , bins=100)

xval = np.arange(-10 , 10 , 0.1);

axs[2][1].plot(xval , norm.pdf(xval , 0 , 1))
axs[2][1].hist(cauchy[(cauchy > -10) & (cauchy < 10)] , bins=100)


xval = np.arange(-5 , 5 , 0.1);
std = 1
axs[2][2].set_title("Loi Gaussienne")
axs[2][2].plot(xval , norm.pdf(xval, mean , std))
std = 0.5
axs[2][2].plot(xval , norm.pdf(xval, mean , std))
std = 0.25
axs[2][2].plot(xval , norm.pdf(xval, mean , std))
std = 0.1
axs[2][2].plot(xval , norm.pdf(xval, mean , std))
std = 0.05
axs[2][2].plot(xval , norm.pdf(xval, mean , std))

plt.show()