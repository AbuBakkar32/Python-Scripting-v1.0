import requests
import csv

# Create your views here.
url = 'https://raw.githubusercontent.com/justmarkham/trump-lies/master/trump_lies.csv'
link = requests.get(url)
decode = (line.decode('utf-8') for line in link.iter_lines())
reader = list(csv.reader(decode))

lists = []
count = 0
for row in reader[1:]:
    temp = {
        'date': row[0],
        'lie': row[1],
        'explanation': row[2],
        'url': row[3]
    }
    lists.append(temp)

for row in reader[1:]:
    if row[0] == '2017-04-29':
        date = row[0:]
print(date)

