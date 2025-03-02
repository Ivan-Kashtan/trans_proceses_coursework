from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT

pdfmetrics.registerFont(TTFont('times', 'times.ttf'))
pdfmetrics.registerFont(TTFont('times_bold', 'timesbd.ttf'))
pdfmetrics.registerFont(TTFont('times_i', 'timesi.ttf'))

f_s = 12
ldng = int(f_s*1.2)

s_c_t = ParagraphStyle('центр', fontName='times', fontSize=f_s, alignment=TA_CENTER, spaceAfter=10, leading=20)
s_c_t_b = ParagraphStyle('центр', fontName='times_bold', fontSize=f_s, alignment=TA_CENTER, spaceAfter=10, leading=20)
s_l = ParagraphStyle('центр', fontName="times", fontSize=f_s, alignment=TA_LEFT, spaceAfter=10, leading=ldng)
s_m = ParagraphStyle('основной', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=2, leading=ldng)
# s_r = ParagraphStyle('по правому', fontName="times", fontSize=f_s, alignment=TA_RIGHT)
s_f_30 = ParagraphStyle('формула 30', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=30,
                        spaceBefore=15,  leading=ldng)
s_f_10 = ParagraphStyle('формула 10', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=10,
                        spaceBefore=5, leading=ldng)
st_5_20 = ParagraphStyle('5 20', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=20,
                        spaceBefore=5, leading=ldng)
st_0_20 = ParagraphStyle('формула 20', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=20,
                        leading=ldng)
st_0_10 = ParagraphStyle('формула 10', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=10,
                        leading=ldng)
st_0_25 = ParagraphStyle('формула 25', fontName='times', fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=25,
                         leading=ldng)
st_20_5 = ParagraphStyle('ст 2', fontName='times', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=20,
                         spaceAfter=5, leading=ldng)
st_15_5 = ParagraphStyle('ст 15 5 ', fontName='times', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=15,
                         spaceAfter=5, leading=ldng)
st_5_10 = ParagraphStyle('ст 5 10', fontName='times', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=5,
                         spaceAfter=10, leading=ldng)
st_5_5 = ParagraphStyle('ст 5 5', fontName='times', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=5,
                         spaceAfter=5, leading=ldng)
st_20_20 = ParagraphStyle('ст 20 20', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=20,
                         spaceAfter=20, leading=ldng)
st_20_0 = ParagraphStyle('ст 2', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=20,
                         leading=ldng)
s_f = ParagraphStyle('заголовок формулы', fontName="times", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=30,
                     spaceBefore=20, leading=ldng)
st_b_20_5 = ParagraphStyle('ст 2', fontName='times_bold', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=20,
                           spaceAfter=5, leading=ldng)

s_b = ParagraphStyle('жирный', fontName="times_bold", fontSize=f_s, alignment=TA_JUSTIFY, spaceAfter=2, leading=ldng)
st_b_5_0 = ParagraphStyle('жирный', fontName="times_bold", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefpre=5,
                          spaceAfter=3, leading=ldng)
s_c_b = ParagraphStyle('центр жирный', fontName="times_bold", fontSize=f_s, alignment=TA_CENTER, spaceAfter=3,
                       spaceBefore=5, leading=ldng)
st_b_10_2 = ParagraphStyle('ст 15 5 ', fontName='times_bold', fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=10,
                           spaceAfter=2, leading=ldng)

st_i_0_3 = ParagraphStyle('ст 5 5 i', fontName="times_i", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=5,
                         spaceAfter=5, leading=ldng)
st_i_15_2 = ParagraphStyle('ст 15 5 i', fontName="times_i", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=15,
                         spaceAfter=2, leading=ldng)
st_i_5_5 = ParagraphStyle('ст 5 5 i', fontName="times_i", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=5,
                         spaceAfter=5, leading=ldng)
st_i_10_5 = ParagraphStyle('ст 5 5 i', fontName="times_i", fontSize=f_s, alignment=TA_JUSTIFY, spaceBefore=5,
                         spaceAfter=5, leading=ldng)
# leading - межстрочный интервал