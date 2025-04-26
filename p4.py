from numpy import sqrt

from p1 import x1_s, e_s
from p2 import x2_s
from p3 import x0_s

m = sqrt(3) * sqrt(1 - (x2_s * x0_s) / ((x2_s * x0_s)**2))
x_d = x2_s*x0_s / (x2_s + x0_s)

i1 = e_s / (x1_s + x_d)
i = m * i1

print(i)
