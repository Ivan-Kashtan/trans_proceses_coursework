# Курсовая станции
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet

# from gen import *
# from load import *
from paragraph_styles import *
from page_number import *
from title_list import *
from eq import *
from in_dat import *
from p1 import *
from p2 import *
from p3 import *
from p4 import *

# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Проектирование электрической части КЭС 5600 МВт')

sp_10 = Spacer(0, 10)
sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1 * cm)
sp_25 = Spacer(0, 25)
sp_50 = Spacer(0, 50)
sp_2 = Spacer(0, 2 * cm)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
cpb = CondPageBreak(10)

# data = [[fml(f'$P_г$, МВт'), fml(f'$S_г$, МВА'), fml(f'$U_{{н.г}}$, кВ'),
#              Paragraph('Схема соединения обмоток', style=s_m),],
#             [fml(f'${p_g}$'), fml(f'${s_g_c}$'), fml(f'${u_g}$'), Paragraph('Y/Y', style=s_m),]]

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     Paragraph('Исходные данные', style=st_b),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схема.png'),
     Paragraph('Рисунок 1 - Исходная схема', style=st_c_5_0),
     Paragraph('Таблица 1 - Исходные данные', style=s_r),
     Table(data = [[fml('Вариант'), fml(f'$L_1$, км'), fml(f'$L_2$, км'), fml(f'$x_0 \\div x_1 $'),
                     fml(f'$S_нагр$, МВА'), fml(f'$\\cos\\phi_{{нагр}}$, МВА'), fml(f'$U_{{ном_\u0020 нагр}}$, кВ')],
                    [fml(f'${l1}$'), fml(f'${l2}$'), fml(f'${x0_x1}$'), fml(f'${s_ld}$'),
                     fml(f'${cos_ld}$'), fml(f'${u_ld}$')]], spaceBefore=5,
            spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),
# , colWidths=70, rowHeights=20,
#      Paragraph('Задание', style=st_b_5_0),

#      Paragraph('''1. При коротком замыкании в точке «К» схемы определить ток в поврежденной фазе для начального
#      момента времени и заданного вида несимметричного короткого замыкания. \n
#      2. Построить векторные диаграммы токов и напряжений в месте короткого замыкания.
#      3. Построить векторную диаграмму напряжений в точке «А» схемы для начального момента времени и заданного вида
#      несимметричного короткого замыкания. (Точка «А» может быть перенесена по решению преподавателя
#      в другое место схемы.)  \n
#      4. Рассчитать доаварийный (нормальный) режим в заданной схеме,
#      приняв 0 ном P P  0,8  и определяя реактивную мощность Q0 из условия Г ном ген U U 1,05 , при этом считать шины,
#      к которым подключена
#      нагрузка, шинами бесконечной мощности (ШБМ). \n
# 5. Рассчитать и построить угловые характеристики электропередачи и определить предел по активной мощности,
# коэффициент запаса и
# максимальный предельный угол электропередачи для случаев: \n
# 1) P = f (), Q = f () без учета АРВ; \n
# 2) P = f () с учетом АРВ пропорционального действия;
# 3) P = f () c учетом АРВ сильного действия.
# 9
# 6. Провести анализ динамической устойчивости электропередачи
# «генератор–шины бесконечной мощности (ШБМ)»:
# 6.1) применить метод площадей для определения предельного угла
# отключения пр.откл  несимметричного короткого замыкания в точке
# «К»;
# 6.2) рассчитать переходный процесс методом последовательных
# интервалов, построить график (t) и определить возможность сохранения динамической устойчивости в случае, если релейная защита отключает поврежденный участок при несимметричном КЗ за нормативное время (нормативное расчетное время КЗ при 110 кВ – 0,18 с,
# 220 кВ – 0,16 с, 500 кВ – 0,12 с);
# 6.3) определить предельное время отключения КЗ, продолжая расчет методом последовательных интервалов (без отключения КЗ) до
# того момента, при котором (t) достигнет значения пр.откл  . Этот момент и определяет предельное время отключения КЗ. ''', style=st_m),
     Paragraph('Выбор оборудования', style=st_b),
     Paragraph('В качестве G1-G2 выбираем 3 турбогенератора ТВФ-100-2. '
               'В качестве G4 выбираем гидрогенератор СВ-780/137-32. Параметры генераторов:', style=st_m),
     Table(data = [[Paragraph('Тип генератора', st_m), fml(f'$S_н$, МВА'), fml(f'$P_н$, МВт'),
                    fml(f'$\\cos \\phi$'), fml(f'U_н$, кВ'), fml(f'$x_d\'\'$'),
                    fml(f'${{x\'}}_d$'), fml(f'${{x}}_d$'), fml(f'${{x}}_q$'),
                    fml(f'$x_2$'), fml(f'$GD^2_d$ т\u00b7м^2'), fml(f'$T_{{d0}}$, с'), fml(f'$n$, об/мин ')],
                   [Paragraph('ТВФ-100-2', st_m), fml(f'${g1['s']}$'), fml(f'${g1['p']}$'),
                    fml(f'{g1['cos']}$'), fml(f'${g1['u']}$'), fml(f'${g1['x_d__']}$'), fml(f'${g1['x_d_']}$'),
                    fml(f'${g1['x_d']}$'), fml(f'${g1['x_q']}$'), fml(f'${g1['x_2']}$'), fml(f'${g1['gd']}$'),
                    fml(f'${g1['t']}$'), fml(f'${g1['n']}$')]],
           style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign='CENTER'),

     # Paragraph('Необходимая номинальная мощность рабочих трансформаторов собственных нужд:', style=st_5_10),
     # fml(f'$S_{{Т_\u0020с.н._\u0020ном}} \u2265 S_{{Г_\u0020ном}} = {s_s_n:.1f}$'),
     # Paragraph('Выбираем трансформатор типа ТРДНС-40000/35 в количестве 2 шт. с номинальным напряжением '
     #           'стороны ВН 24 кВ, а стороны НН - 6,3 кВ', style=st_5_5),
     # с. 134 Неклепаев

     # .setStyle([('LEADING', 10)]),
     # Paragraph('https://ciu.nstu.ru/kaf/persons/676/a/file_get/293101?nomenu=1', style=s_m)]
     ]
doc.build(f, onLaterPages=addPageNumber)
