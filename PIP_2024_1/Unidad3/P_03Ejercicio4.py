from matplotlib import pyplot as plt
from archivos import fileFunc

fileFunc.prueba()

x = [i for i in range(-10,11)]
print(x)
y = [x1**2 for x1 in x]
print(y)
plt.plot(x,y)
plt.show()