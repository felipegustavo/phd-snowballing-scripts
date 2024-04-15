ouput_files = [
    'out/ids_linked_links_backward_snowballing.csv',
    'out/ids_linked_links_forward_snowballing.csv',
    'out/ids_related_links_backward_snowballing.csv',
    'out/ids_related_links_forward_snowballing.csv'
]

def seta_duplicadas_arquivo(filename):
    with open(filename, 'r') as file:
        header = file.readline().replace('\n', '')
        map = dict()
        for line in file:
            parts = line.split(',')
            map[parts[0]] = parts[1].replace('\n', '')
    
        header = header + ',duplicada'
        lines = [header]

        for k, v in map.items():
            lines.append('{},{},{}'.format(k, v, 'Sim' if k in duplicated_set else 'Não'))
        
        file.close()
        #print(lines)

    with open(filename, 'w') as file:
        file.write('\n'.join(lines))
        file.close()


duplicated_set = set()
with open('out/duplicated_ids.csv', 'r') as file:
    file.readline()
    for line in file:
        duplicated_set.add(line.split(',')[0])

for filename in ouput_files:
    seta_duplicadas_arquivo(filename)

#print(duplicated_set)