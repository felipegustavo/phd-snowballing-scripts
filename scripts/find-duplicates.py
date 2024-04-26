ouput_files = {
    'LINKED_BS': 'out/LINKED BS.csv',
    'LINKED_FS': 'out/LINKED FS.csv',
    'RELATED_BS': 'out/RELATED BS.csv',
    'RELATED_FS': 'out/RELATED FS.csv'
}

posts = dict()

for type, filename in ouput_files.items():
    with open(filename, 'r') as file:
        file.readline() # me livrando do header
        for line in file:
            parts = line.strip().split(',')
            id = int(parts[0])
            hits = int(parts[1])

            if (posts.get(id) == None):
                posts[id] = dict()

            posts[id][type] = hits

csv_lines = ['question id,LINKED BS hits,LINKED FS hits,RELATED BS hits,RELATED FS hits']
for key, value in posts.items():
    if len(value) > 1:
        csv_lines.append('{},{},{},{},{}'.format(
            key, value.get('LINKED_BS', 0), value.get('LINKED_FS', 0),
            value.get('RELATED_BS', 0), value.get('RELATED_FS', 0)
        ))

with open('out/Duplicações.csv', 'w') as file:
    file.write('\n'.join(csv_lines))
    file.close()
