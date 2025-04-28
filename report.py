# Курсовая станции
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak, Image
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet

from paragraph_styles import *
from page_number import *
from title_list import *
from eq import *
from in_dat import *

from p1 import *

# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Курсовая перехода')

sp_10 = Spacer(0, 10)
sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1 * cm)
sp_25 = Spacer(0, 25)
sp_30 = Spacer(0, 30)
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

f = [
    KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     Paragraph('Исходные данные', style=st_b),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Схема.png',
           width=15*cm, height=10*cm, kind='proportional'),
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
     Paragraph('Выбор оборудования', style=st_c_b),
     Paragraph('В качестве G1-G2 выбираем 3 турбогенератора ТВФ-100-2. '
               'В качестве G4 выбираем гидрогенератор СВ-780/137-32. Параметры генераторов:', style=st_m),
     Paragraph('Таблица 2 - Параметры генераторов', style=s_r),
     Table(data = [[Paragraph('Тип генератора', st_m), fml(f'$S_н$, МВА'), fml(f'$P_н$, МВт'),
                    fml(f'$\\cos \\phi$'), fml(f'U_н$, кВ'), fml(f'$x_d\'\'$'),
                    fml(f'${{x\'}}_d$'), fml(f'${{x}}_d$'), fml(f'$x_2$'), fml(f'$GD^2_d$ т\u00b7м^2'),
                    fml(f'$T_{{d0}}$, с'), fml(f'$n$, об/мин ')],
                   [Paragraph('ТВФ-100-2', st_m), fml(f'${g1['s']}$'), fml(f'${g1['p']}$'),
                    fml(f'{g1['cos']}$'), fml(f'${g1['u']}$'), fml(f'${g1['x_d__']}$'), fml(f'${g1['x_d_']}$'),
                    fml(f'${g1['x_d']}$'), fml(f'${g1['x2']}$'), fml(f'${g1['gd']}$'),
                    fml(f'${g1['t_d0']}$'), fml(f'${g1['n']}$')],
                   [Paragraph('СВ-655/110-32', st_m), fml(f'${g2['s']}$'), fml(f'${g2['p']}$'),
                    fml(f'{g2['cos']}$'), fml(f'${g2['u']}$'), fml(f'$-$'), fml(f'${g2['x_d_']}$'),
                    fml(f'${g2['x_d']}$'), fml(f'${g2['x2']}$'), fml(f'${g2['gd']}$'),
                    fml(f'${g2['t_d0']}$'), fml(f'$-$')]

                   ],
           style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign='CENTER'),

     Paragraph('Расчет несимметричного короткого замыкания', style=st_b),
     Paragraph('Для расчета используем метод ППОЕ', style=st_5_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Базисные напряжения.png',
           width=121.8*mm, height=58.9*mm, kind='proportional'),
     Paragraph('Рисунок 2 - Исходная схема с базисными напряжениями', style=st_c_5_0),
     Paragraph('Базисные величины', style=st_i_5_20),
     fml(f'$S_Б = {s_b}$'),
     sp_20,
     fml(f'$U_{{Б1}} = {u_b[0]}; \\quad U_{{Б2}} = {u_b[1]}; \\quad U_{{Б3}} = {u_b[2]}$'),
     sp_20,
     fml(f'$I_{{Б1}} = \\dfrac{{S_{{Б1}} }} {{\\sqrt{{3}} U_{{Б1}} }}; \\quad '
         f'I_{{Б1}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[0]}}} = {i_b[0]:.2f}$ кА'),
     sp_20,
     fml(f'$I_{{Б2}} = \\dfrac{{S_{{Б2}} }} {{\\sqrt{{3}} U_{{Б2}} }}; \\quad '
         f'I_{{Б2}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[1]}}} = {i_b[1]:.2f}$ кА'),
     sp_20,
     fml(f'$I_{{Б3}} = \\dfrac{{S_{{Б3}}}} {{\\sqrt{{3}} U_{{Б3}} }}; \\quad '
         f'I_{{Б3}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[2]}}} = {i_b[2]:.2f}$ кА'),
     Paragraph('Расчет сопротивлений прямой последовательности', style=st_i_5_5),
     Paragraph('При расчете сразу учтем количество параллельных элементов ЭС', style=st_5_20),
     fml(f'$n_{{Г1}} = {n_g1}; \\quad n_{{Т1}} = {n_t1}$'),

     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\1-я последовательность.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рисунок 3 - Схема замещения прямой последовательности', style=st_c_5_20),
     fml(f'$S_{{Г1}}^* = \\dfrac {{S_{{Г1}} }} {{S_Б}}; \\quad  '
         f'S_{{Г1}}^* = \\dfrac {{ {g1['s']} }} {{{s_b}}} = {s_g_r[0]}$'),
     sp_30,
     fml(f'$U_{{г1}}^* = \\dfrac {{U_{{Г1}}}} {{U_{{Б2}}}}; \\quad  '
         f'U_{{г1}}^* = \\dfrac {{ {g1['u']} }} {{u_b[1]}} = {u_g_r[0]}$'),
     sp_30,
     fml(f'$P_{{Г1}}^* = S_{{Г1}}^* \\cos\\phi; \\quad  '
         f'P_{{Г1}}^* = {g1['s']} \\cdot {g1['cos']} = {g1['p']:.2f}$'),
     sp_30,
     fml(f'$Q_{{Г1}}^* = S_{{Г1}}^* \\sin\\phi; \\quad  '
         f'P_{{Г1}}^* = {g1['s']} \\cdot {g1['sin']:.3f} = {g1['q']:.2f}$'),
     sp_30,
     fml(f'$S_{{Г2}}^* = \\dfrac {{S_{{Г2}}}} {{S_Б}}; \\quad  '
         f'S_{{Г2}}^* = \\dfrac {{ {g2['s']:.2f} }} {{{s_b}}} = {s_g_r[1]:.2f}$'),
     sp_30,
     fml(f'$U_{{г2}}^* = \\dfrac {{U_{{Г2}}}} {{U_{{Б2}}}}; \\quad  '
         f'U_{{г2}}^* = \\dfrac {{ {g2['u']} }} {{{u_b[2]}}} = {u_g_r[1]}$'),
     sp_30,
     # fml(f'$P_{{Г2}}^* = S_{{Г2}}^* \\cos\\phi; \\quad  '
     #     f'P_{{Г2}}^* = {g2['s']} \\cdot {g2['cos']} = {g2['p']:.2f}$'),
    fml(f'$P_{{Г2}}^* = {g2['p']}$'),
     sp_30,
    fml(f'$Q_{{Г2}}^* = {g2['q']}$'),
     # fml(f'$Q_{{Г2}}^* = S_{{Г2}}^* \\sin\\phi; \\quad  '
     #     f'Q_{{Г2}}^* = {g2['s']} \\cdot {g2['sin']:.3f} = {g2['p']:.2f}$'),
     sp_30,
     # fml(f'$E_1 = \\left|{{E\'\'}} \\right| = \\dfrac{{1}} {{{n_g1}}}  = sqrt{{\\left(U_г^* + '
     #     f'\\dfrac {{Q_г^* x_d\'\'}} '
     #     f'{{U_г^*}} \\right)^2 + \\left({{\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}} \\right)^2}}; \\quad  '
     #     f'E_1 = \\dfrac{{1}} {{{n_g1}}} sqrt{{\\left({u_g_r[0]} + \\dfrac {{{q_g_r[0]} \\cdot {x_d__[0]}}} '
     #     f'{{{u_g_r}}} \\right)^2 + \\left({{\\dfrac {{{p_g_r[0]} {x_d__[0]}}} {{{u_g_r[0]}}} \\right)^2}}$'),
    fml(f'$E_1 = \\left|{{E\'\'}} \\right| = \\dfrac {{1}} {{{n_g1}}} \\sqrt{{\\left(U_г^* + '
         f'\\dfrac {{Q_г^* x_d\'\'}} {{U_г^*}}\\right)^2 + \\left(\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}}\\right)^2}}; \\quad'
        f'E_1 = \\left|{{E\'\'}} \\right| = \\dfrac {{1}} {{{n_g1}}} \\sqrt{{\\left({u_g_r[0]} + '
         f'\\dfrac {{{q_g_r[0]} {x_d__[0]}}} {{{u_g_r}}}\\right)^2 + \\left(\\dfrac {{{p_g_r[0]} {x_d__[0]}}} '
        f'{{{u_g_r[0]}}}\\right)^2}}$'),
        # f'E_1 = \\dfrac{{1}} {{{n_g1}}} sqrt{{ ({u_g_r[0]} + \\dfrac{{{q_g_r[0]} \\cdot {x_d__[0]} }} '
        #  f'{{{u_g_r}}} \\)^2 + ({{\\dfrac {{{p_g_r[0]} {x_d__[0]}}} {{{u_g_r[0]}}} )^2}}$'),
# f'E_1 = \\left|{{E\'\'}} \\right| = \\dfrac{{1}} {{{n_g1}}}  = sqrt{{\\left(U_г^* + \\dfrac {{Q_г^* x_d\'\'}} '
        #  f'{{U_г^*}} \\right)^2 + \\left({{\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}} \\}}right)^2$'),
sp_30,
     fml(f'$x_1 = \\dfrac {{x_d\'\' S_{{Г1}}^*}} {{n_{{Г1}} }}; \\quad x_1 = \\dfrac {{x_d\'\' S_{{Г1}}^*}} {{ {n_g1} }} = {x[0]:.2f}$')
     ]
doc.build(f, onLaterPages=addPageNumber)
