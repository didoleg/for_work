from datetime import datetime
import openpyxl
import os


def find_csv():
    for file in os.listdir():
        if file.endswith('.csv'):
            return file


current_date = datetime.now().date()
count = 0
operator_mnc = int(input('Введите MNC оператора:\n(1 - МТС; 2 - МЕГАФОН; 20 - ТЕЛЕ2; 99 - БИЛАЙН)\n'))
mnc = {1: 'МТС', 2: 'МЕГАФОН', 20: 'ТЕЛЕ2', 99: 'БИЛАЙН'}
list_GSM = []
list_LTE = []

with open(f'{find_csv()}') as f1:
    with open(f'LAC_bs_{mnc[operator_mnc]}.txt') as f2:
        list_bs = [int(bs.strip('\n')) for bs in f2]
        for line in f1:
            row = [el.strip('""') for el in line.split(';')]
            if row[0].isdigit():
                date = datetime.strptime(row[8], '%Y-%m-%d %H:%M:%S').date()
                lac, cell_id, end_date, azimut = int(row[0]), row[1], datetime.strptime(row[8], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y'), int(row[3])
                lat, lon, address, start_date = row[5].replace('.', ','), row[4].replace('.', ','), row[6], datetime.strptime(row[7], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
                sector, power, height, frequency = int(row[2]), row[9], row[10], row[11]

                if current_date < date and lac in list_bs and len(cell_id) < 6:
                    count += 1
                    if height == '':
                        height = 30
                    if power == '':
                        power = 43
                    if sector <= 0:
                        sector = 60
                    row_GSM = [count, f'250-{operator_mnc}-{lac}-{cell_id}', cell_id, lac, 17, int(cell_id) % 10,
                               lon, lat, azimut, 5000, address, '', '', frequency, height, sector, '', power]
                    list_GSM.append(row_GSM)

                elif current_date < date and lac in list_bs and len(cell_id) > 6:
                    if height == '':
                        height = 30
                    if power == '':
                        power = 43
                    if sector <= 0:
                        sector = 60
                    row_LTE = [mnc[operator_mnc], 'LTE', f'250-{operator_mnc}-{cell_id}', 250, operator_mnc,
                               cell_id, lon, lat, azimut, 1000, sector, 'Тыва', address, start_date]
                    list_LTE.append(row_LTE)

wb_GSM = openpyxl.load_workbook(f'{mnc[operator_mnc]}_GSM.xlsx')
for row in list_GSM:
    sheet = wb_GSM.active.append(row)
wb_GSM.save(f'{mnc[operator_mnc]}_GSM.xlsx')

wb_LTE = openpyxl.load_workbook(f'{mnc[operator_mnc]}_LTE.xlsx')
for row in list_LTE:
    sheet = wb_LTE.active.append(row)
wb_LTE.save(f'{mnc[operator_mnc]}_LTE.xlsx')
