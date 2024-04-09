ouput_files = {
    'LINKED_BS': 'out/ids_linked_links_backward_snowballing.csv',
    'LINKED_FS': 'out/ids_linked_links_forward_snowballing.csv',
    'RELATED_BS': 'out/ids_related_links_backward_snowballing.csv',
    'RELATED_FS': 'out/ids_related_links_forward_snowballing.csv'
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

with open('out/duplicated_ids.csv', 'w') as file:
    file.write('\n'.join(csv_lines))
    file.close()
