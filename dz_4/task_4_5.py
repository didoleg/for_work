import requests
import sys
from datetime import datetime


def course_money(args):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    money_list = response.text.split('ID=')
    date_headers = response.headers["date"].split()
    date = datetime.strptime(f'{date_headers[2]}-{date_headers[1]}-{date_headers[3]}', '%b-%d-%Y').date()
    money_list.remove(money_list[0])
    money_dict = {}

    for money in money_list:
        find_key = money.split('<CharCode>')
        find_val = money.split('/Name><Value>')
        key = find_key[1][0:3]
        val = find_val[1][0:find_val[1].find('<')]
        money_dict.setdefault(key, val)

    if money_dict.get(args) is not None:
        dict_num = money_dict.get(args)
        int_num = int(dict_num[0:dict_num.find(',')])
        float_num = round((int(dict_num[(dict_num.find(',')) + 1:]) / 10000), 2)
        number = int_num + float_num
        print(f'{args} {number}, {date}')
    else:
        print(money_dict.get(args))


course_money(sys.argv[1].upper())