with open('out/Duplicações.csv') as file:
    headers = file.readline().replace('\n', '').split(',')
    map = dict()

    for line in file.readlines():
        parts = line.replace('\n', '').split(',')
        types = []
        for i in range(1, 5):
            if parts[i] != '0':
                types.append(headers[i])

        key = '+'.join(types)
        map[key] = map.get(key, 0) + 1

print(map)
