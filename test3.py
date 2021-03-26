import numpy as np
from pylab import *
from qutip import *
import pickle

N = 3
# parameters

wc = 1
wl = 1
Delta1 = 0.5
Delta2 = 0.5
g1 = 0.005
g2 = 0.005
gamma = 0.00001
kappa = 0.00001
inc1 = 0.1
t = np.linspace(0, 100, 100)

# operators
a1 = tensor(destroy(N), qeye(2), qeye(2))
sm1 = tensor(qeye(N), sigmam(), qeye(2))
sm2 = tensor(qeye(N), qeye(2), sigmam())
sz1 = tensor(qeye(N), sigmaz(), qeye(2))
sz2 = tensor(qeye(N), qeye(2), sigmaz())

# time-independent Hamiltonian
H1 = wc * a1.dag() * a1 + 0.5 * (a1.dag() * sm1 + sm1.dag() * a1) \
     + 0.5 * (a1.dag() * sm2 + sm2.dag() * a1) \
     + Delta1 * sz1 + Delta2 * sz2
HI = -(a1.dag() * sm1 + sm1.dag() * a1) - (a1.dag() * sm2 + sm2.dag() * a1) \
     + sz1 - sz2


def g_1(t, args):
    return g1 * t


H2 = [H1, [HI, g_1]]
# enviroment is in vaccum state
n_1 = n_2 = 0
c_ops1 = [[a1, a_1], \
          np.sqrt(0.00001) * sm1, \
          np.sqrt(0.00001) * sm2, \
          np.sqrt(0.0001) * sz1, \
          np.sqrt(0.0001) * sz2]

# state
rho0 = ((tensor(basis(N, 0), basis(2, 1), basis(2, 0)) - tensor(basis(N, 0), basis(2, 0), basis(2, 1)))).unit()
rhot = tensor(basis(N, 1), basis(2, 0), basis(2, 0))
rhot1 = tensor(basis(N, 0), basis(2, 0), basis(2, 0))
rho = ((tensor(basis(N, 1), basis(2, 0), basis(2, 0))) \
       + (tensor(basis(N, 0), basis(2, 1), basis(2, 0))) - (tensor(basis(N, 0), basis(2, 0), basis(2, 1)))).unit()

result1 = mesolve(H2, rho0, t, [], [rho0 * rho0.dag(), rhot * rhot.dag(), rhot1 * rhot1.dag(), rho * rho.dag()])
fig, ax = plt.subplots()
plt.plot(t, result1.expect[0], label='|0↓↑>-|0↑↓>', linewidth=4.0)
plt.plot(t, result1.expect[1], label='|1↓↓>', linewidth=4.0)
plt.plot(t, result1.expect[2], label='|0↓↓>', linewidth=4.0)
plt.plot(t, result1.expect[3], label='|Ψ>', linewidth=4.0)
plt.legend(fontsize='large')
plt.show()