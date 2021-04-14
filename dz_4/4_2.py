import requests

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
money_list = response.text.split('ID=')
money_list.remove()
money_dict = {}

# with open('file.txt', 'w') as f:
#     for el in money_list:
#         f.write(f'{el}\n')

for money in money_list:
    key = money.split('>')
    val = money.split('>')
    print(len(key))
    #print(val[10])


