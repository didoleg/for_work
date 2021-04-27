with open('nginx_logs.txt') as f:
    ip_list = [line[0:line.find(' -')] for line in f]
    find_max_requests = max({ip_list.count(ip): ip for ip in ip_list})
    find_spam_ip = {ip_list.count(ip): ip for ip in ip_list}[find_max_requests]

print(f'IP адрес спамера: {find_spam_ip}, кол-во отправленных запросов: {find_max_requests}')







