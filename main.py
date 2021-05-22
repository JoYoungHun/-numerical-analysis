import numpy as np
import matplotlib.pyplot as plt
g = 9.8
cd = 0.25
m = 68
# euler's method
v0 = 0
v1 = (1 - 0) * (g - cd / m * v0 ** 2) + v0
v2 = (2 - 1) * (g - cd / m * v1 ** 2) + v1
v3 = (3 - 2) * (g - cd / m * v2 ** 2) + v2
v4 = (4 - 3) * (g - cd / m * v3 ** 2) + v3
vel_euler = [v0, v1, v2, v3, v4]

g = 9.8
cd = 0.25
m = 68
# differential equation method
t = np.arange(0,5)
vel = np.sqrt(g*m/cd)*np.tanh( np.sqrt(g*cd/m)*t )
plt.plot(t, vel, 'ro-', t, vel_euler, 'b>-')
plt.grid()
plt.legend(['vel_differential','vel_euler'])
plt.show()