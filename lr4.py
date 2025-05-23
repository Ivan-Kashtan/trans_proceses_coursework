'''
Лабораторная работа № 4
ИССЛЕДОВАНИЕ ПЕРЕХОДНЫХ ПРОЦЕССОВ
ПРИ ВКЛЮЧЕНИИ ТРАНСФОРМАТОРА
ЦЕЛЬ РАБОТЫ
Исследование характера изменения тока включения трансформатора в зависимости от режима работы вторичных обмоток (холостой ход,
нагрузочный режим), а также от момента включения трансформатора в
сеть.
ЗАДАНИЕ
1. Путем осциллографирования тока первичной обмотки трансформатора изучить характер изменения мгновенного значения тока
трансформатора при включении его в сеть.
2. Оценить влияние загрузки трансформатора на переходный процесс, уделить особое внимание включению в режиме холостого хода
при возможности появления бросков тока намагничивания.
'''

from numpy import array, round, sqrt, average, linspace, where
from matplotlib.pyplot import plot, grid, show, savefig, title, xlabel, ylabel
from scipy.interpolate import CubicSpline, Akima1DInterpolator


u = array([[45.4, 40.5, 35.2, 30, 25.3, 20.2, 15.1, 10.1, 5, 0],
           [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]])

u_av = (u[1] + u[0, ::-1]) / 2
u_n = 36
i = sqrt(2)*array([[0.36, 0.25, 0.19, 0.14, 0.11, 0.09, 0.06, 0.04, 0.03, 0.01],
                   [0, 0.03, 0.04, 0.06, 0.08, 0.11, 0.14, 0.18, 0.26, 0.37]])
i_av = (i[1] + i[0, ::-1]) / 2

x = linspace(i_av[0], i_av[-1], 500)

# f = CubicSpline(i_av, u_av, bc_type='natural')
f = CubicSpline(i_av, u_av)
# f = Akima1DInterpolator(i_av, u_av)

u = f(x)
i_n = x[where(round(u, 1) == u_n)][0]
#
# u[] =
# plot(u, sqrt(2)*i, 'k')
# plot(x, u, 'k')
plot(i_n, u_n, 'xk')
plot(i_av, u_av, '.k')

grid()
title('ВАХ трансформатора')
xlabel('$i$, А')
ylabel('$U$, В')
# show()
savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 4\Точки ВАХ.png', dpi=600)
print(i)
