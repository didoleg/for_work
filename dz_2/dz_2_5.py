price_list = [25, 34.4, 87.1, 76, 34, 90.34, 22.76, 56.67, 76.02, 89.09, 62.13, 93.94, 12.8, 57.8, 46.51]

result = []
for price in price_list:
    if type(price) is not int:
        cent_price = str(price)[str(price).find(".") + 1:]     # Отделение дробной части вещественного числа, через строку
        if len(cent_price) > 1:
            element = f'{int(price)} руб {cent_price} коп'
            result.append(element)
        else:
            element = f'{int(price)} руб {cent_price}0 коп'
            result.append(element)
    else:
        element = f'{price} руб {0:02} коп'
        result.append(element)

result_str = ', '.join(result)
price_list.sort()                                               # Сортировка цен по возрастанию
sort_price_min = sorted(price_list, reverse=True)               # Сортировка цен по убыванию
max_price_5 = sorted(sorted(price_list, reverse=True)[:5])      # Вывод цен 5и самых дорогих товаров


print(result_str)                               # Результат пункта 'A'
print(price_list)                               # Результат пункта 'B'
print(id(price_list[0]), id(price_list[0]))     # Доказательство, что объект списка после сортировки не изменился
print(sort_price_min)                           # Результат пункта 'C'
print(max_price_5)                              # Результат пункта 'D'

