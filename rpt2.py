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
    'rprt2.pdf',
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

f = [Paragraph('Расчет несимметричного короткого замыкания', style=st_b),
     Paragraph('Для расчета используем метод ППОЕ', style=st_5_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Экспортировано\Базисные напряжения.png',
           width=121.8*mm, height=58.9*mm, kind='proportional'),
     Paragraph('Рисунок 2 - Исходная схема с базисными напряжениями', style=st_c_5_0),
     Paragraph('Базисные величины', style=st_i_5_20),
     fml(f'$S_Б = {s_b}$'),
     sp_20,
     fml(f'$U_{{Б1}} = {u_b[0]}; \\quad U_{{Б2}} = {u_b[1]}; \\quad U_{{Б3}} = {u_b[2]}$'),
     sp_20,
     fml(f'$I_{{Б1}} = \\dfrac{{S_{{Б1}} }} {{\\sqrt{{3}} U_{{Б1}} }}; \\quad '
         f'I_{{Б1}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[0]}}} = {i_b[0]:.2f}$ кА'),
     sp_30,
     fml(f'$I_{{Б2}} = \\dfrac{{S_{{Б2}} }} {{\\sqrt{{3}} U_{{Б2}} }}; \\quad '
         f'I_{{Б2}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[1]}}} = {i_b[1]:.2f}$ кА'),
     sp_30,
     fml(f'$I_{{Б3}} = \\dfrac{{S_{{Б3}}}} {{\\sqrt{{3}} U_{{Б3}} }}; \\quad '
         f'I_{{Б3}} = \\dfrac {{{s_b}}} {{\\sqrt{{3}} \\cdot {u_b[2]}}} = {i_b[2]:.2f}$ кА'),
     Paragraph('Расчет сопротивлений прямой последовательности', style=st_20_5),
     Paragraph('При расчете сразу учтем количество параллельных элементов ЭС', style=st_0_10),
     fml(f'$n_{{Г1}} = {n_g1}; \\quad n_{{Т1}} = {n_t1}$'),
     sp_20,
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Экспортировано\1-я последовательность.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рисунок 3 - Схема замещения прямой последовательности', style=st_c_5_10),
    #  fml(f'$S_{{Г1}}^* = \\dfrac {{S_{{Г1}} }} {{S_Б}}; \\quad  '
    #      f'S_{{Г1}}^* = \\dfrac {{ {g1['s']} }} {{{s_b}}} = {s_g_r[0]}$'),
    #  sp_30,
    #  fml(f'$U_{{г1}}^* = \\dfrac {{U_{{Г1}}}} {{U_{{Б2}}}}; \\quad  '
    #      f'U_{{г1}}^* = \\dfrac {{ {g1['u']} }} {{u_b[1]}} = {u_g_r[0]}$'),
    #  sp_30,
    #  fml(f'$P_{{Г1}}^* = S_{{Г1}}^* \\cos\\phi; \\quad  '
    #      f'P_{{Г1}}^* = {g1['s']} \\cdot {g1['cos']} = {g1['p']:.2f}$'),
    #  sp_30,
    #  fml(f'$Q_{{Г1}}^* = S_{{Г1}}^* \\sin\\phi; \\quad  '
    #      f'P_{{Г1}}^* = {g1['s']} \\cdot {g1['sin']:.3f} = {g1['q']:.2f}$'),
    #  sp_30,
    #  fml(f'$S_{{Г2}}^* = \\dfrac {{S_{{Г2}}}} {{S_Б}}; \\quad  '
    #      f'S_{{Г2}}^* = \\dfrac {{ {g2['s']:.2f} }} {{{s_b}}} = {s_g_r[1]:.2f}$'),
    #  sp_30,
    #  fml(f'$U_{{г2}}^* = \\dfrac {{U_{{Г2}}}} {{U_{{Б2}}}}; \\quad  '
    #      f'U_{{г2}}^* = \\dfrac {{ {g2['u']} }} {{{u_b[2]}}} = {u_g_r[1]}$'),
    #  sp_30,
    #  # fml(f'$P_{{Г2}}^* = S_{{Г2}}^* \\cos\\phi; \\quad  '
    #  #     f'P_{{Г2}}^* = {g2['s']} \\cdot {g2['cos']} = {g2['p']:.2f}$'),
    #
    # fml(f'$P_{{Г2}}^* = {g2['p']}$'),
    #  sp_30,
    # fml(f'$Q_{{Г2}}^* = {g2['q']}$'),
     # fml(f'$Q_{{Г2}}^* = S_{{Г2}}^* \\sin\\phi; \\quad  '
     #     f'Q_{{Г2}}^* = {g2['s']} \\cdot {g2['sin']:.3f} = {g2['p']:.2f}$'),
     sp_30,
     # fml(f'$E_1 = \\left|{{E\'\'}} \\right| = \\dfrac{{1}} {{{n_g1}}}  = sqrt{{\\left(U_г^* + '
     #     f'\\dfrac {{Q_г^* x_d\'\'}} '
     #     f'{{U_г^*}} \\right)^2 + \\left({{\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}} \\right)^2}}; \\quad  '
     #     f'E_1 = \\dfrac{{1}} {{{n_g1}}} sqrt{{\\left({u_g_r[0]} + \\dfrac {{{q_g_r[0]} \\cdot {x_d__[0]}}} '
     #     f'{{{u_g_r}}} \\right)^2 + \\left({{\\dfrac {{{p_g_r[0]} {x_d__[0]}}} {{{u_g_r[0]}}} \\right)^2}}$'),
    fml(f'$E = \\left|{{E\'\'}} \\right| = \\sqrt{{\\left(U_г^* + '
         f'\\dfrac {{Q_г^* x_d\'\'}} {{U_г^*}}\\right)^2 + \\left(\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}}\\right)^2}}$'),
    sp_30,
    fml(f'$E_1 = {n_g1} \\sqrt{{\\left({u_g_r[0]} + '
         f'\\dfrac {{{q_g_r[0]:.2f} \\cdot {x_d__[0]} }} {{{u_g_r[0]}}}\\right)^2 + \\left(\\dfrac {{{p_g_r[0]} '
        f'\\cdot{x_d__[0]}}}'
        f'{{{u_g_r[0]}}}\\right)^2}} = {e[0]:.3f}$'),
    sp_30,
    fml(f'$E_2 = \\sqrt{{\\left({u_g_r[1]} + '
         f'\\dfrac {{{q_g_r[1]:.2f} \\cdot {x_d__[1]} }} {{{u_g_r[1]}}}\\right)^2 + \\left(\\dfrac {{{p_g_r[1]:.3f} \\cdot '
        f'{x_d__[1]}}}'
        f'{{ {u_g_r[1]} }}\\right)^2}} = {e[1]:.3f}$'),
    sp_30,
    fml(f'$E_3 = 0.85 \\dfrac {{U_н}} {{U_{{Б1}}}}; \\quad '
         f'E_3 = {0.85} \\dfrac {{{u_ld}}} {{ {u_b[0]} }} = {e_ld:.3f}$'),

        # f'E_1 = \\dfrac{{1}} {{{n_g1}}} sqrt{{ ({u_g_r[0]} + \\dfrac{{{q_g_r[0]} \\cdot {x_d__[0]} }} '
        #  f'{{{u_g_r}}} \\)^2 + ({{\\dfrac {{{p_g_r[0]} {x_d__[0]}}} {{{u_g_r[0]}}} )^2}}$'),
# f'E_1 = \\left|{{E\'\'}} \\right| = \\dfrac{{1}} {{{n_g1}}}  = sqrt{{\\left(U_г^* + \\dfrac {{Q_г^* x_d\'\'}} '
        #  f'{{U_г^*}} \\right)^2 + \\left({{\\dfrac {{P_г^* x_d\'\'}} {{U_г^*}} \\}}right)^2$'),
    sp_30,
    fml(f'$x_1 = x_d\'\' \\dfrac {{S_б}} {{n_{{Г1}} S_{{Г1}}}}; \\quad '
         f'{x_d__[0]} \\dfrac {{{s_b}}} {{{n_g1} \\cdot {g1['s']}}} = {x[0]:.3f}$'),
    sp_30,
    fml(f'$x_2 = \\dfrac {{ u_{{к}} }} {{100}} \\dfrac {{S_б}} {{ n_{{Т1}} S_{{Т1}} }}; \\quad'
        f'x_2 = \\dfrac {{ {t1['u_sc']} }} {{100}} \\dfrac {{ {s_b} }} {{ {n_t1} {t1['s']} }} = {x[1]:.3f}$'),
    sp_30,
    fml(f'$x_3 = x_0 \\left(l_1 + l_2\\right) \\dfrac {{S_Б}} {{U_{{ср._\u0020 л}}^2 }}; \\quad'
        f'x_3 = {x_ln} \\left({l1} + {l2}\\right) \\dfrac {{{s_b}}} {{{u_b[0]}}} = {x[2]:.3f}$'),
    sp_30,
    fml(f'$x_4 = \\dfrac {{u_{{к}}}} {{100}} \\dfrac {{S_б}} {{S_{{Т2}}}}; \\quad '
        f'x_4 = \\dfrac {{{t2['u_sc_h-l']}}} {{100}} \\dfrac {{{s_b}}} {{ {t2['s']} }} = {x[3]:.3f}$'),
    sp_30,
    fml(f'$x_5 = x_d\'\' \\dfrac {{S_б}} {{S_{{г2}}}}; \\quad '
         f'{x_d__[1]} \\dfrac {{ {s_b} }} {{{g2['s']:.3f}}} = {x[4]:.3f}$'),
    sp_30,
    fml(f'$x_6 = {0.35} \\dfrac {{S_б}} {{S_{{нагр._\u0020 ном}}}}; \\quad '
         f'x_6 = {0.35} \\dfrac {{ {s_b} }} {{ {{{s_ld}}} }} = {x[5]:.3f}$'),
    Paragraph('Эквивалентируем схему', st_20_20),
    Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Экспортировано\1) Эквивалентная схема.png',
           width=94.3*mm, height=62.3*mm, kind='proportional'),
    Paragraph('Рисунок 4 - Сэквивалентированная схема замещения прямой последовательности', style=st_c_5_20),
    # fml(f'$x_7 = \\dfrac {{x_6 \\left(x_2 + x_3\\right)}} {{x_6 + x_2 + x_3}}; \\quad '
    #      f'x_7 = \\dfrac {{{x[5]:.3f} \\left({x[1]:.3f} + {x[2]:.3f} \\right)}} {{{x[5]} + {x[1]} + {x[2]}}}$'),
    # sp_30,
     fml(f'$x_7 = x_1 + x_2 + x_3; \\quad x_7 = {x[0]:.3f} + {x[1]:.3f} + {x[2]:.3f} = {x_e[0]:.3f}$'),
     sp_20,
     fml(f'$x_8 = x_4 + x_5; \\quad x_8 = {x[3]:.3f} + {x[4]:.3f} ={x_e[1]:.3f}$'),
     sp_25,
     fml(f'$x_9 = \\dfrac {{x_8 x_6}} {{x_8 + x_6}}; \\quad '
          f'x_9 = \\dfrac {{{x_e[1]:.3f} + {x[5]:.3f}}} {{{x_e[1]:.3f} + {x[5]:.3f}}} = {x_e[2]:.3f}$'),
     sp_30,
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Экспортировано\1) эквивалентная 2.png',
           width=86.2*mm, height=62.3*mm, kind='proportional'),
     Paragraph('Рисунок 5 - Сэквивалентированная схема замещения прямой последовательности', style=st_c_5_20),
     fml(f'$x_9 = \\dfrac {{x_8 x_6}} {{x_8 + x_6}}; \\quad '
          f'x_9 = \\dfrac {{{x_e[1]:.3f} + {x[5]:.3f}}} {{{x_e[1]} + {x[5]} }} = {x_e[2]}$'),
     sp_30,
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Переходные процессы\Курсовая\Схемы\Экспортировано\1) схема 3.png',
           width=60.1*mm, height=27.8*mm, kind='proportional'),
     Paragraph('Рисунок 6 - Сэквивалентированная схема замещения прямой последовательности', style=st_c_5_20),
     fml(f'$x_{{10}} = x_7 + x_9; \\quad {x_e[0]:.3f} + {x_e[2]:.3f} = {x1_s:.3f}$'),
     sp_30,
     fml(f'$E_4 = \\dfrac {{E_1 x_7 + E_2 x_4}} {{x_7 + x_6}}; \\quad '
          f'E_4 = \\dfrac {{ {e[0]:.3f} \\cdot {x_e[0]:.3f} + {e[1]:.3f} \\cdot {x[5]:.3f}}} {{{x_e[0]:.3f} + {x[5]:.3f}}} = {  e_e:.3f}$'),
     sp_25,
     fml(f'$E_5 = E_4 + E_1; \\quad E_5 = {e_e:.3f} + {e[0]:.3f} = {e_s:.3f$}'),

        ]
doc.build(f, onLaterPages=addPageNumber)
