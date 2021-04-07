some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result_list = []
for element in some_list:
    for i in element:
        code_i = ord(i)                                       # Преобразования символа в utf-8 кодировку
        if 47 < code_i < 58 or code_i == 43 or code_i == 45:  # Поиск значений имеющих числовое значение и знаки '+' '-'
            if code_i == 43 or code_i == 45:                  # Поиск значений имеющих знак
                new_element = list(element)
                new_element.insert(1, '0')
                result_list.extend([f'"{""}"', f'"{"".join(new_element)}"', f'"{""}"'])
                break
            elif len(element) > 1:                             # Поиск 2х значных чисел
                result_list.extend([f'"{""}"', f'"{element}"', f'"{""}"'])
                break
            else:                            # Поиск чисел 1но значных чисел
                result_list.extend([f'"{""}"', f'"0{element}"', f'"{""}"'])
        else:
            result_list.append(element)
            break

target_list = result_list.copy()
for element in target_list:
    if element == '""':
        target_list.remove(element)
result_str = ' '.join(target_list)

print(some_list)
print(result_list)
print(result_str)






