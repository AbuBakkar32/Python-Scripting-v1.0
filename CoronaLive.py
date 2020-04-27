import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
html_page = requests.get(url).text
soup = BeautifulSoup(html_page, 'lxml')
get_table = soup.find("table", id="main_table_countries_today")
get_table_data = get_table.tbody.find_all("tr")

dic = {}
for i in range(len(get_table_data)):
    try:
        key = get_table_data[i].find_all("a", href=True)[0].string
    except:
        key = get_table_data[i].find_all("td")[0].string
    values = [j.string for j in get_table_data[i].find_all("td")]
    dic[key] = values

# column_names = ["Total_Cases","New Cases","Total Deaths","Total Recovery"]
table = pd.DataFrame(dic).iloc[1:, :]
print(table)

