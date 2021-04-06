some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_str = ' '.join(some_list)

#print(result_str)

new_list = []
for num, element in enumerate(some_list):
    for i in element:
        code_i = ord(i)
        if 47 < code_i < 58 or code_i == 43 or code_i == 45:
            if code_i == code_i == 43 or code_i == 45:
                new_list.append(f'{element}')
                break
            elif len(element) > 1:
                new_list.append(element)
                break
            elif len(element) == 1:
                new_list.append(f'0{element}')



# for number in new_list:
#     if number in some_list:


print(new_list)


