import numpy as np
import matplotlib.pyplot as plt 
'exec(%matplotlib inline)'

# Transition Matrix
props = np.array([
    [0, 0.3, 0.4, 0.3, 0], # s_0 => s'
    [0, 0, 0.4, 0.3, 0.3], # s_1 => s'
    [0, 0.2, 0, 0.7, 0.1], # s_2 => s'
    [0, 0.1, 0.1, 0, 0.8], # s_3 => s'
    [0, 0, 0, 0, 0] # s_4 => s' 
])

# Rewards Matrix
R = np.array([
    [0, -1, -1, -1, 0], # R(s_0) => s'
    [0, 0, -1, -1, 1], # R(s_1) => s'
    [0, -1, 0, -1, 1], # R(s_2) => s'
    [0, -1, -1, 0, 1], # R(s_3) => s'
    [0, 0, 0, 0, 0]
])


v = np.zeros(props.shape[0])
v_old = v.copy()
gamma = 0.9
delta = 1e-5
delta_t = 1
dif = 1

# Apply the Bellman equation
while delta_t > delta:
    for s in range(len(props)):
        v[s] = np.sum([props[s][sp] * (R[s][sp] + gamma * v_old[sp])\
            for sp in range(len(props[s]))
        ])
    delta_t = np.sum(np.abs(v - v_old))
    v_old = v.copy()
print(v)    