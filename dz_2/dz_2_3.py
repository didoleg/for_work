some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for num, element in enumerate(some_list):
    for i in element:
        code_i = ord(i)
        if 47 < code_i < 58 or code_i == 43 or code_i == 45:
            if code_i == 43 or code_i == 45:
                new_element = list(some_list.pop(num))
                new_element.insert(1, '0')
                some_list.insert(num, f'"{"".join(new_element)}"')
                break
            elif len(element) == 1:
                some_list.pop(num)
                some_list.insert(num, f'"0{element}"')
            else:
                some_list.pop(num)
                some_list.insert(num, f'"{element}"')
                break


result_str = ' '.join(some_list)
print(some_list)
print(result_str)

