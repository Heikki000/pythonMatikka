import numpy as np
import matplotlib.pyplot as plt
x =np.linspace(-5,10,100)
y = x**-2
x2=np.linspace(-5,10,100)
y2=-x2**-3
x3=np.linspace(-5,10, 100)
y3= x3**-4
ax=plt.subplot()

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# samat mittasuhteet
ax.set_aspect('equal')
ax.set_ylim([-15, 15])

plt.plot(x, y, color='blue')
plt.plot(x2,y2, color='green')
plt.plot(x3,y3, color='red')
plt.show()