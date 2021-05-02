import re

with open('nginx_logs.txt') as file:
    RE_IP = re.compile(r'^(?:\d+.){3}\d+')
    RE_DATE = re.compile(r'\d{2}/[A-Za-z]+/\d{4}:(?:\d{2}:){2}\d{2} \+\d{4}')
    RE_TYPE = 2
    RE_CODE = re.compile(r's*\d{3}')
    RE_SIZE = re.compile(r' \d\ ')

    for raw in file:
        print(RE_SIZE.findall(raw))
        parsed_raw = (f'{RE_IP.findall(raw)[0]}', f'{RE_DATE.findall(raw)[0]}', f'{RE_CODE.findall(raw)[0]}', f'{RE_SIZE.findall(raw)[0]}')

        print(parsed_raw)