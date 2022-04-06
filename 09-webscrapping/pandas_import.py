import pandas as pd
file_names = ['CazuriCovid.xls', 'CazuriCovid1.xls', 'CazuriCovid2.xls',  'CazuriCovid3.xls', 'CazuriCovid4.xls',
              'CazuriCovid5.xls',  'CazuriCovid6.xls']
data_all = pd.concat((pd.read_csv(i) for i in file_names)).reset_index(drop=True)  # Import
print(data_all)
data_all.to_csv('CazuriCovidCombi.xls')
