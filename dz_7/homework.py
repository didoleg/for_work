import os

files = []
for r, d, f in os.walk('folder'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)
print(max_size)
i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    print(range(len(str(max_size))))
    i *= 10
    out_dict[i] = 0

for file in files:
    print(file)
    print(len(str(file)))
    out_dict[10 ** len(str(file))] += 1


print(out_dict)

