from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, num=500)

epsilon = 0.5
alpha = 0.0000000000001
delta = 0.000000000000001
beta = 0.5
y0 = [beta/delta, epsilon/alpha]


def sim(variables, t):
    x = variables[0]
    y = variables[1]

    dxdt = epsilon * x - alpha * x * y
    dydt = delta * x * y - beta * y

    return([dxdt, dydt])


figure, axs = plt.subplots(2, 6)

colors = ['black', 'black', 'purple', 'purple', 'green', 'green']

for i in range(1, 7):
    delta = 0.000000000000001
    delta /= i
    y = odeint(sim, y0, t)

    line1, = axs[0][i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[0][i-1].plot(t, y[:, 1], '--', color=colors[i-1])

for i in range(7, 13):
    delta = 0.000000000000001
    delta /= i
    y = odeint(sim, y0, t)

    line1, = axs[1][i-7].plot(t, y[:, 0], color=colors[i-7])
    line2, = axs[1][i-7].plot(t, y[:, 1], '--', color=colors[i-7])

plt.show()
