# Опыт 1
from math import atan, degrees

from numpy import array, linspace
from pandas import DataFrame, ExcelWriter
from matplotlib.pyplot import plot, show, grid, legend, title, savefig, xlabel, ylabel
from scipy.interpolate import CubicSpline, Akima1DInterpolator

e1 = DataFrame({'P':[1, 3, 6, 8, 12, 13, 14, 15],
                  'd': [10, 20, 30, 40, 50, 60, 70, 80]})
e2 = DataFrame({'P':[2, 7, 11, 14, 17, 18, 19],
                'd': [10, 20, 30, 40, 50, 60, 70]})
e3 = DataFrame({'P': [2, 6, 8, 12, 16, 18, 20, 22],
                'd': [10, 20, 30, 40, 50, 60, 70, 80]})
u = 42
e4 = DataFrame({'P': [1, 3, 6, 10, 16, 18],
                'd': [10, 20, 30, 40, 50, 55]})
e5 = DataFrame({'P': [0, 4, 7, 10, 12, 13, 14, 15, 16, 17],
                'd': [-30, -20, -10, 0, 10, 20, 30, 40, 50, 60]})
x = linspace(min(e3['d']), max(e3['d']), 500)
f = Akima1DInterpolator(e3['d'], e3['P'], method="akima")
# f1 = CubicSpline(e1['d'], e1['P'])

p = 10
q = 5
u_s = 42
u_g = 46
i_a = 0.38
d = 30
du = 9.4
i_q = 70.3
phi_g = degrees(atan(q / p))
r'''
with ExcelWriter(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 7\Данные.xlsx',
                 mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
    # e1.to_excel(writer, sheet_name='1')
    # e2.to_excel(writer, sheet_name='2')
    # e3.to_excel(writer, sheet_name='3')
    # e4.to_excel(writer, sheet_name='4')
    e5.to_excel(writer, sheet_name='5')
'''

plot(x, f(x), 'k')
plot(e3['d'], e3['P'], '.k')
title('Характеристика P генератора при большем $i_f$')
grid()
xlabel(r'$P$, Вт')
ylabel(r'$\delta$, град.')
# legend()
# show()

# savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\ЛР\ЛР 7\3.svg')
# show()
print(e1)
