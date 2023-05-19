from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
from math import pi

y0 = [10, 2]

t = np.linspace(0, 50, num=1000)

epsilon = 0.8
alpha = 0.4
delta = 0.15
beta = 0.6


def sim(variables, t):
    x = variables[0]
    y = variables[1]

    dxdt = epsilon * x - alpha * x * y
    dydt = delta * x * y - beta * y

    return([dxdt, dydt])


figure, axs = plt.subplots(6, 6)

colors = ['black', 'black', 'purple', 'purple', 'green', 'green']
parameters = [epsilon, alpha, delta, beta]

for i in range(1, 7, 2):
    epsilon = 0.4
    alpha = 0.4
    delta = 0.15
    beta = 0.6

    epsilon *= i
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[0, i].plot(st, nd, color=colors[i])

    line1, = axs[0, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[0, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[0, i-1].title.set_text(f'ε = {round(epsilon, 1)}')
    print((2*pi)/((epsilon*beta)**0.5))
print('\n')
for i in range(1, 7, 2):
    epsilon = 0.8
    alpha = 0.2
    delta = 0.15
    beta = 0.6

    alpha *= i
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[1, i].plot(st, nd, color=colors[i])

    line1, = axs[1, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[1, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[1, i-1].title.set_text(f'α = {round(alpha, 1)}')
    print((2*pi)/((epsilon*beta)**0.5))
print('\n')
for i in range(1, 7, 2):
    epsilon = 0.8
    alpha = 0.4
    delta = 0.075
    beta = 0.6

    delta *= i
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[2, i].plot(st, nd, color=colors[i])

    line1, = axs[2, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[2, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[2, i-1].title.set_text(f'δ = {round(delta, 3)}')
    print((2*pi)/((epsilon*beta)**0.5))
print('\n')
for i in range(1, 7, 2):
    epsilon = 0.8
    alpha = 0.4
    delta = 0.15
    beta = 0.2

    beta *= i
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[3, i].plot(st, nd, color=colors[i])

    line1, = axs[3, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[3, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[3, i-1].title.set_text(f'β = {round(beta, 1)}')
    print((2*pi)/((epsilon*beta)**0.5))
print('\n')
for i in range(1, 7, 2):
    epsilon = 0.8
    alpha = 0.4
    delta = 0.15
    beta = 0.6
    y0 = [5, 2]

    y0[0] *= i
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[4, i].plot(st, nd, color=colors[i])

    line1, = axs[4, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[4, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[4, i-1].title.set_text(f'x0 = {round(y0[0], 1)}')
    print((2*pi)/((epsilon*beta)**0.5))
print('\n')
for i in range(1, 7, 2):
    epsilon = 0.8
    alpha = 0.4
    delta = 0.15
    beta = 0.6
    y0 = [10, 2]

    y0[1] *= i*2
    y = odeint(sim, y0, t)

    st = y[:, 0]
    nd = y[:, 1]

    axs[5, i].plot(st, nd, color=colors[i])

    line1, = axs[5, i-1].plot(t, y[:, 0], color=colors[i-1])
    line2, = axs[5, i-1].plot(t, y[:, 1], '--', color=colors[i-1])
    axs[5, i-1].title.set_text(f'y0 = {round(y0[1], 1)}')
    print((2*pi)/((epsilon*beta)**0.5))

plt.setp(axs[0, 0], ylabel='∆ε')
plt.setp(axs[1, 0], ylabel='∆α')
plt.setp(axs[2, 0], ylabel='∆δ')
plt.setp(axs[3, 0], ylabel='∆β')
plt.setp(axs[4, 0], ylabel='∆ prey')
plt.setp(axs[5, 0], ylabel='∆ predator')
figure.tight_layout(pad=0.03)
plt.show()
