import requests
from lxml import etree

xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
curs = xml_response.find("Valute[@ID='R01200']/Value").text

print(f"Один Гонконгский доллар равен {curs} рублей")
#print(response_1.headers['Content-Type'])

if __name__ == '__main__':
    pass
https://pythonru.com/biblioteki/prodvinutoe-rukovodstvo-po-biblioteke-python-requests