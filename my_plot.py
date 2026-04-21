import numpy as np
import japanize_matplotlib
datasets = np.array([[4,7], [8,10], [13,11], [17,14]])
x = datasets[:,0]
y = datasets[:,1]

import matplotlib.pyplot as plt
plt.scatter(x,y, color="black", label="データセット")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")

def function(x):
    return (x-10)**2
  
x2 = np.linspace(4,17,100)
y2 = function(x2)
plt.plot(x2,y2, color="blue", linewidth=3,label="プロット例")
plt.show()
