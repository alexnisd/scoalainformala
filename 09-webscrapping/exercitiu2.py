import pandas as pd
# raw_data = {'name': ['Rutuja', 'Neeraj',
#                      'Renna', 'Pratik'],
#             'age': [20, 19, 22, 21],
#             'favorite_color': ['blue', 'red',
#                                'yellow', "green"],
#             'grade': [88, 92, 95, 70],
#             'birth_date': ['01-02-2000', '08-05-1997',
#                            '04-28-1996', '12-16-1995']}
# df = pd.DataFrame(raw_data,
#                   index=['Rutuja', 'Neeraj',
#                            'Renna', 'Pratik'])
# df['year'] = pd.DatetimeIndex(df['birth_date']).year
# df['month'] = pd.DatetimeIndex(df['birth_date']).month
# df.head()
# print(df)
description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017', '2018 ', '2019 '])

dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']), ]


def get_country_data(x, y):
    if y == 'Albania':
        z = x[0]
        print(z)
    elif y == 'Austria':
        z = x[1]
        print(z)
    elif y == 'Bosnia':
        z = x[2]
        print(z)
    elif y == 'Belgia':
        z = x[3]
        print(z)
    elif y == 'Bulgaria':
        z = x[4]
        print(z)
    elif y == 'Elvetia':
        z = x[5]
        print(z)
    elif y == 'Cipru':
        z = x[6]
        print(z)
    elif y == 'Cehia':
        z = x[7]
        print(z)
    elif y == 'Germania':
        z = x[8]
        print(z)
    elif y == 'Danemarca':
        z = x[9]
        print(z)
    elif y == 'Ceuta':
        z = x[10]
        print(z)
    elif y == 'Estonia':
        z = x[11]
        print(z)
    elif y == 'Grecia':
        z = x[12]
        print(z)
    elif y == 'Spania':
        z = x[13]
        print(z)
    elif y == 'Finlanda':
        z = x[14]
        print(z)
    elif y == 'Franta':
        z = x[15]
        print(z)
    elif y == 'Croatia':
        z = x[16]
        print(z)
    elif y == 'Ungaria':
        z = x[17]
        print(z)
    elif y == 'Islanda':
        z = x[18]
        print(z)
    elif y == 'Irlanda':
        z = x[19]
        print(z)
    elif y == 'Italia':
        z = x[20]
        print(z)
    elif y == 'Lituania':
        z = x[21]
        print(z)
    elif y == 'Luxemburg':
        z = x[22]
        print(z)
    elif y == 'Latvia':
        z = x[23]
        print(z)
    elif y == 'Muntenegru':
        z = x[24]
        print(z)
    elif y == 'Macedonia de Nord':
        z = x[25]
        print(z)
    elif y == 'Malta':
        z = x[26]
        print(z)
    elif y == 'Olanda':
        z = x[27]
        print(z)
    elif y == 'Norvegia':
        z = x[28]
        print(z)
    elif y == 'Polonia':
        z = x[29]
        print(z)
    elif y == 'Portugalia':
        z = x[30]
        print(z)
    elif y == 'Romania':
        z = x[31]
        print(z)
    elif y == 'Serbia':
        z = x[32]
        print(z)
    elif y == 'Suedia':
        z = x[33]
        print(z)
    elif y == 'Slovenia':
        z = x[34]
        print(z)
    elif y == 'Slovaica':
        z = x[35]
        print(z)
    elif y == 'Turcia':
        z = x[36]
        print(z)
    elif y == 'Marea Britanie':
        z = x[37]
        print(z)
    elif y == 'Kosovo':
        z = x[38]
        print(z)
    else:
        print('Tara invalida!')
        #  print(i.elements)
    # print(x[1][1][0])
    # print(x[1][1][1])
    # print(x[1][1][2])
    # print(x[1][1][3])
    # print(x[1][1][4])
    # print(x[1][1][5])
    # print(x[1][1][6])
    # print(x[1][1][7])
    # print(x[1][1][8])


get_country_data(dataset, "Romania")
# {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}

