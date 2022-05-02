from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-26-ianuarie-ora-13-00/")
# table = browser.find_element_by_xpath('by=By.XPATH, value=xpath')
table = browser.find_element(by=By.XPATH, value='//*[@id="post-25198"]/div/div/table[1]/tbody')
table_text = table.text
lista = table_text.split('\n')
print(table_text)
print(lista)
header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25198"]/div/div/table[1]/tbody/tr[1]')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
# print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        print(lista[i])
        dictionar[header[int(j)]].append(lista[i])
print(header)
print(table_text)
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("CazuriCovid.xls") #am luat cazurile pe rand dar nu am mai facut alt cod, pur si simplu am scris in acelasi cod si le-am facut xls-uri separate. (ex.: CazuriCovid2, 3, 4.. etc.)


# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
# # print(r.text)
# link = BeautifulSoup(r.text, "html.parser")
# # print(link)
#
# title = link.find_all("div", attrs={"class": "contentDiv"})
# header = []
# dataset = []
# for i in title:
#     for tr_index in i.find_all("table"):
#         for td_index in tr_index.find_all("tr"):
#             # print(td_index)
#             td_list = []
#             if td_index.find_all("th"):
#                 header = [th_index.get_text() for th_index in td_index.find_all("th")]
#             for index, td_value in enumerate(td_index.find_all("td")):
#                 print(index, td_value)
#                 if index == 0:
#                     td_list.append(td_value.get_text())
#                 else:
#                     td_list.append(float(td_value.get_text().replace(",", ".")))
#             dataset.append(td_list)
# # print(header)
# print(dataset)
# df = pd.DataFrame(dataset, columns=header)
# # print(df)
# df.to_csv("CazuriCovid1.xls", header=header)
