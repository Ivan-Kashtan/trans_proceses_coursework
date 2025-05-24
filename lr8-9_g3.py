# Опыт 2 - 4-й пункт методички
# 1-фазное кз
from numpy import array, linspace
from scipy.interpolate import CubicSpline, Akima1DInterpolator
from matplotlib.pyplot import plot, show, grid, legend, title, savefig, xlabel, ylabel, figure, gca

p = array([8, 8, 7, 8])
t = array([0.025, 0.1, 0.15, 0.275])
d = array([20, 20, 18, 20])


# x3 = linspace(d[0, 0], d[0, -1], 50)[::-1]
# x1 = linspace(d[0, 0], d[0, -1], 50)[::-1]
# x3 = linspace(t[0, 0], t[0, -1], 50)[::-1]
x = linspace(t[0], t[-1], 50)[::-1]
# f3 = CubicSpline(t[0], p[0])
f = CubicSpline(t, p)
# f = Akima1DInterpolator(t, p)

# plot(x, f3(x), 'k')
plot(x, f(x), 'k')
plot(t, p, '.k')
title('Зависимость $P_{пред}(t_{АПВ})$')
xlabel(r'$t_{АПВ}$, с')
ylabel('$P_{пред}$, Вт')
grid()

savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 8-9\3_1.png', dpi=600)
show()

print(d[1])
# print(d[0, ::-1])
# print(d[:, -1])
