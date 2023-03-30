from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page=requests.get(url)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')
print(len(star_table))

temp_list=[]
table_rows=star_table[7].find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)
S=[]
D=[]
M=[]
R=[]
L=[]

for i in range(1,len(temp_list)):
    S.append(temp_list[i][0])
    D.append(temp_list[i][5])
    M.append(temp_list[i][7])
    R.append(temp_list[i][8])
   
    
df2=pd.DataFrame(list(zip(S,D,M,R)),columns=['S','D','M','R'])
print(df2)
df2.to_csv('bright_stars.csv')