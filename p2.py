from numpy import sqrt, array, empty
from in_dat import *
from p1 import *
x2 = array([g1['x2'], g2['x2']])/100


x = empty(6)
x[0] = x2[0] * s_g_r[0] / 3  # g1
x[1] = t1['u_sc'] / 100 * s_b * t1['s'] / 2  # t1
x[2] = x_ln * (l1+l2) * s_b / u_b[0]**2  # line
x[3] = t2['u_sc_h-l'] / 100 * s_b * t2['s'] / 2  # t2
x[4] = x2[1] * s_g_r[1]  # g2
x[5] = 0.35 * s_b / s_ld

x2_s = sum(x)
# x_e = empty(2)
# x_e[0] = x[0] + x[1]
# x_e[1] = sum(x[2:])

# e1 = sqrt()
# x1 =
# u_g = array([g1['u'], ])

# e_b = e * array([g1['u'], g2['u']]) /
# print(f'{1.2 * p_ld=}')
# print(f'{1.2 * q_ld=}')
# print(3 * g1['s'])

# print(g1['s'])
print(x[2:])

print(u_g_r)
print(s_g_r)

# print(3 * g1['p'] + g2['p'])
# print(3 * g1['q'] + g2['q'])
