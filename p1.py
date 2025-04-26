from numpy import sqrt, array, empty
from in_dat import *

s_ld = 360  # МВА
cos_phi = 0.85
u_n = 220

p_ld = s_ld * cos_phi
q_ld = s_ld * (1 - cos_phi**2)**(1/2)

g1['s'] = sqrt(g1['q']**2 + g1['p']**2)
g2['s'] = sqrt(g2['q']**2 + g2['p']**2)

s_b = 125
u_b = array([230, 10.5, 10.5])
s_g_r = array([(g1['s'] / s_b), (g2['s'] / s_b)])
cos_g = array([g1['cos'], g2['cos']])
p_g_r = s_g_r * cos_g
sin_g = sqrt(1 - (cos_g**2))
q_g_r = s_g_r * sin_g
u_g_r = array([g1['u'], g2['u']]) / s_b

x_d__ = array([g1['x_d__'], g2['x_d__']])/100
e = sqrt((u_g_r + q_g_r * x_d__ / u_g_r)**2 + (p_g_r * x_d__ / u_g_r)**2)

x = empty(6)
x[0] = x_d__[0] * s_g_r[0] / 3  # g1
x[1] = t1['u_sc'] / 100 * s_b * t1['s'] / 2  # t1
x[2] = x_ln * (l1+l2) * s_b / u_b[0]**2  # line
x[3] = t2['u_sc_h-l'] / 100 * s_b * t2['s'] / 2  # t2
x[4] = x_d__[1] * s_g_r[1]  # g2
x[5] = 0.35 * s_b / s_ld

x_e = empty(2)
x_e[0] = (x[5] * (x[1] + x[2])) / (x[5] + x[1] + x[2])
x_e[1] = sum(x[2:5])

x1_s = sum(x_e)

e_ld = 0.85 * u_ld / u_b[0]

e_s = (e[0] * 3 * sum(x[:2]) + e[1] * sum(x[2:5])
       / (sum(x[:2]) + sum(x[2:5])))

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
# print(x[2:])

# print(x[2:5])
# print(s_g_r)

# print(3 * g1['p'] + g2['p'])
# print(3 * g1['q'] + g2['q'])
