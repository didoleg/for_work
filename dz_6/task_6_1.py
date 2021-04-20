with open('nginx_logs.txt') as f:
    data = [(line[0:line.find(' -')], line[line.find('"') + 1:line.find(' /')], line[line.find('/d'):line.find(' HTTP')]) for line in f]

print(data)










