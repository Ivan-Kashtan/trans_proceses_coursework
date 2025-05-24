from numpy import array, linspace, sin, pi, radians
# from scipy.interpolate import CubicSpline
from matplotlib.pyplot import plot, show, grid, legend, title, savefig, xlabel, ylabel, figure, gca, xticks, MultipleLocator

p = [18, 19]
d = array([70, 40])
x = linspace(0, pi, 100)
n_l = 7
x_l = linspace(0, pi, n_l)
y = array([0, max(p)])
labels = linspace(0, 180, n_l)
plot(x, p[0]*sin(x), '--k', label='Работа Л1 и Л2')
plot(x, p[1]*sin(x), 'k', label='Обрыв линии Л2')
# plot([radians(d[0]), radians(d[0])], y)
# plot(radians(d[1]), y)
# ax = gca()
# ax.set_aspect('equal', adjustable='box')
title('Зависимость $P(\\delta)$')
xlabel(r'$\delta$, град.')
ylabel('$P$, Вт')
xticks(x_l, labels)
ax = gca()  # Создание экземпляра осей для возможности его редактирования
ax.xaxis.set_major_locator(MultipleLocator(pi/6))  # Основная цена деления оси Ox
ax.xaxis.set_minor_locator(MultipleLocator(pi/18))  # Дополнительная цена деления оси Ox (t)
# ax.yaxis.set_major_locator(MultipleLocator(100))  # Основная цена деления оси Oy
# ax.yaxis.set_minor_locator(MultipleLocator(20))  # Дополнительная цена деления оси Oy (t)
grid()
legend()
savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 8-9\0.png', dpi=600)
show()
