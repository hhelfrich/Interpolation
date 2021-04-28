import numpy as np

Gamma_1 = np.array([[0. + 0.j, 0.+0.j, 0+0.j, 1.+0.j],
                    [0.+0.j, 0.+0.j, 1+0.j, 0.+0.j],
                    [0.+0j, -1.+0.j, 0.+0.j, 0.+0.j],
                    [-1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])

Gamma_2 = np.array([[0. + 0.j, 0.+0.j, 0+0.j, 0.-1.j],
                    [0.+0.j, 0.+0.j, 0+1.j, 0.+0.j],
                    [0.+0j, 0.+1.j, 0.+0.j, 0.+0.j],
                    [0.-1.j, 0.+0.j, 0.+0.j, 0.+0.j]])

g2_ct = np.transpose(np.conjugate(Gamma_2))
g2_inv = np.linalg.inv(Gamma_2)

print(g2_ct)
print(g2_inv)
print(-Gamma_2)
print(np.dot(Gamma_1, Gamma_2))