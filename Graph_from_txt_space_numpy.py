import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('05072021_Gustavo_hahella_no_CPD.txt', skiprows=1, unpack=True)
plt.plot(x,y,)

plt.xlabel('Time (min)')
plt.ylabel('[UV]')
plt.title('05072021_Gustavo_hahella_no_CPD')

plt.show()


