some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element in some_list:
    *trash, Name = element.split()
    print(f'Привет, {Name.capitalize()}!')


