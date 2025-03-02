from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.platypus.flowables import Image, ParagraphAndImage, Spacer
# from reportlab.lib.units import cm
from paragraph_styles import s_l, s_c_t, s_c_t_b

'''
t_l = SimpleDocTemplate(
        "title_list.pdf",
        pagesize=A4,
        rightMargin=1*cm, leftMargin=3*cm,
        topMargin=1*cm, bottomMargin=1.5*cm)
'''

mn = Paragraph('Министерство науки и высшего образования Российской Федерации ', style=s_c_t)
t_u = Paragraph('Федеральное государственное бюджетное образовательное учреждение высшего образования', style=s_c_t)
un = Paragraph('Новосибирский государственный технический университет', style=s_c_t)
kaf = Paragraph('Кафедра ЭлСт', style=s_c_t)
# s_2 = Spacer(0, 2*cm)
# s_3 = Spacer(0, 3*cm)
# s_5 = Spacer(0, 5*cm)
# s_6_5 = Spacer(0, 6.5*cm)
s_50 = Spacer(0, 50)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
# s_130 = Spacer(0, 120)
s_150 = Spacer(0, 150)
tp = Paragraph('Курсовая работа', style=s_c_t)
title = Paragraph('Переходные процессы в электроэнергетике', style=s_c_t_b)
var = Paragraph('Вариант 32', style=s_c_t)
fac = Paragraph('Факультет: ФЭН', style=s_l)
gr = Paragraph('Группа: Эн1-22', style=s_l)
st = Paragraph('Студент: Кашталапов И.С.', style=s_l)
tchr = Paragraph('Преподаватель: Долгов А.П.', style=s_l)
mk = Paragraph('Отметка о защите:', style=s_l)
sity = Paragraph('Новосибирск, 2025 г.', style=s_c_t)

# t_l = [mn, t_u, un, s_80, kaf, s_130, tp, title, var, s_100, fac, gr, st, tchr, mk, s_80, s]
# t_l.build(fls)
