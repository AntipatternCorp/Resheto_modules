'''
++ ДД/++ НН/
++ ЛЦ/02 Пушкин/03 Александр/04 Сергеевич/05 26.05.1799/06 Москва/07 29.02.1837/08 Санкт-Петербург/
.../
++ КК/++ ЯЯ/
'''

def ufod_gen(collect_name, bd_names, attributes):
    filename = collect_name + '_ufod.txt'
    ufod_str = '++ ДД/++ НН/'
    i=0
    for bd in bd_names:
        ufod_str = ufod_str + '\n++ '+ str(bd) +'/'
        for atr_number, atr_value in attributes[i].items():
            ufod_str = ufod_str + str(atr_number) + ' ' +str(atr_value)+ '/'
        i=i+1
    ufod_str = ufod_str + '\n++ КК/++ ЯЯ/'
    with open(filename, mode="w", encoding="cp1251") as f:
        f.write(ufod_str)
    return True

'''
ufod test
c = 'писатели'
b = ['ЛЦ', 'ЛЦ', 'РГ']
a = [{'02': 'Пушкин', '03': 'Александр', '04' : 'Сергеевич', '05' : '26.05.1799', '06' : 'Москва'},
{'02': 'Пушкин', '03': 'Александр', '04' : 'Сергеевич', '07': '29.02.1837', '08': 'Санкт-Петербург'},
{'02': 'Белые тапочки и черный гранит', '03':'ОАО'}]
ufod_gen(c,b,a)
'''