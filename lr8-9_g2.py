# Опыт 2
# 1-фазное кз
from numpy import array, linspace
from scipy.interpolate import CubicSpline
from matplotlib.pyplot import plot, show, grid, legend, title, savefig, xlabel, ylabel, figure, gca

p = array([[11, 11, 9],
           [15, 14, 15]])
t = array([[0.025, 0.05, 0.175],
          [0.025, 0.05, 0.175]])
d = array([[30+1e-10, 30, 25],
           [40-1e-10, 40, 45]])


# x3 = linspace(d[0, 0], d[0, -1], 50)[::-1]
# x1 = linspace(d[0, 0], d[0, -1], 50)[::-1]
# x3 = linspace(t[0, 0], t[0, -1], 50)[::-1]
x = linspace(t[1, 0], t[1, -1], 50)[::-1]
# f3 = CubicSpline(t[0], p[0])
f1 = CubicSpline(t[1], p[1])

plot(t[1], p[1], '.k')
plot(x, f1(x), 'k')
title('Зависимость $P_{пред}(t_{откл})$ при 1-фазном кз')
xlabel(r'$t_{откл}$, с')
ylabel('$P_{пред}$, Вт')
grid()
savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 8-9\2_2.png', dpi=600)
show()

print(d[1])
# print(d[0, ::-1])
# print(d[:, -1])
