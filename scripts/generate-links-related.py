import database
import json

QUERY_BACKWARD_SNOWBALLING = '''
select * from post_link_related
where post_id in (select id from post_startset)
'''

QUERY_FORWARD_SNOWBALLING = '''
select * from post_link_related
where post_id not in (select id from post_startset);
'''

FILE_OUTPUT_BACKWARD = 'out/ids_related_links_backwardsnowballing.txt'
FILE_OUTPUT_FORWARD = 'out/ids_related_links_forwardsnowballing.txt'

connection = database.connect()
cursor = connection.cursor()

op = input('Digite a operação (1 - backward snowballing, 2 - forward snowballing): ')

if op == '1':
    query = QUERY_BACKWARD_SNOWBALLING
    filepath = FILE_OUTPUT_BACKWARD
else:
    query = QUERY_FORWARD_SNOWBALLING
    filepath = FILE_OUTPUT_FORWARD

cursor.execute(query)
rows = cursor.fetchall()

questions_map = dict()

if op == '1':

    # Iterando por discussões relacionadas apontadas pelo startset
    for row in rows:
        data = json.loads(row[1])
        items = data['items']
        for item in items:
            id = item['question_id']
            questions_map[id] = questions_map.get(id, 0) + 1

else:

    # criando set a partir startset
    cursor.execute('select * from post_startset')
    rows_startset = cursor.fetchall()
    set_startset = set()
    for row_startset in rows_startset:
        set_startset.add(row_startset[0])

    # Iterando por discussões relacionadas que apontam pro startset
    for row in rows:
        data = json.loads(row[1])
        items = data['items']
        for item in items:
            id = item['question_id']
            if id in set_startset:
                questions_map[id] = questions_map.get(id, 0) + 1
    

with open(filepath, 'w') as file:
    file.write('question_id\tqtd_related_hits\n')
    for k, v in questions_map.items():
        file.write('{}\t{}\n'.format(k, v))
    file.flush()
    file.close()

cursor.close()
connection.close()
