ouput_files = [
    'out/LINKED BS.csv',
    'out/LINKED FS.csv',
    'out/RELATED BS.csv',
    'out/RELATED FS.csv'
]

def remove_duplicadas_arquivo(filename):
    with open(filename, 'r') as file:
        header = file.readline().replace('\n', '')
        map = dict()
        for line in file:
            parts = line.split(',')
            map[parts[0]] = parts[1].replace('\n', '')
    
        lines = [header]

        for k, v in map.items():
            if k not in duplicated_set:
                lines.append('{},{}'.format(k, v))
        
        file.close()
        #print(lines)

    with open(filename, 'w') as file:
        file.write('\n'.join(lines))
        file.close()


duplicated_set = set()
with open('out/Duplicações.csv', 'r') as file:
    file.readline()
    for line in file:
        duplicated_set.add(line.split(',')[0])

for filename in ouput_files:
    remove_duplicadas_arquivo(filename)

#print(duplicated_set)