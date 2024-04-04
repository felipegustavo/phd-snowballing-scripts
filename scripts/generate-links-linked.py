import database

# Carrega lista de linked links apontados pelo start set
SELECT_BACKWARD_SNOWBALLING = '''
select pl.related_post_id  from post_link pl
where
    pl.post_id in (select distinct ps1.id from post_startset ps1) and
    pl.link_type_id = 1
order by pl.creation_date desc
'''

# Carrega lista de linked links apontados pelo start set dentro do start set
SELECT_BACKWARD_SNOWBALLING_STARTSET = '''
select pl.related_post_id from  post_link pl 
where
    pl.post_id  in (select distinct ps1.id from post_startset ps1) and
    pl.link_type_id  = 1 and
    pl.related_post_id  in (select distinct ps2.id from post_startset ps2)
order by pl.creation_date  desc
'''

SELECT_FORWARD_SNOWBALLING= '''
select pl.related_post_id  from post_link pl
where
	pl.link_type_id  = 1 and
    pl.post_id  not in (select distinct ps1.id from post_startset ps1) and
    pl.related_post_id  in (select distinct ps2.id from post_startset ps2)
order by pl.creation_date  desc
'''

FILE_OUTPUT_BACKWARD = 'out/ids_linked_links_backwardsnowballing.txt'
FILE_OUTPUT_FORWARD = 'out/ids_linked_links_forwardsnowballing.txt'

connection = database.connect()
cursor = connection.cursor()

op = input('Digite a operação (1 - backward snowballing, 2 - forward snowballing): ')

if op == '1':
    query = SELECT_BACKWARD_SNOWBALLING
    filepath = FILE_OUTPUT_BACKWARD
else:
    query = SELECT_FORWARD_SNOWBALLING
    filepath = FILE_OUTPUT_FORWARD

cursor.execute(query)
rows_post = cursor.fetchall()

questions_map = dict()

for row in rows_post:
    id = row[0]
    questions_map[id] = questions_map.get(id, 0) + 1

with open(filepath, 'w') as file:
    file.write('question_id\tqtd_linked_hits\n')
    for k, v in questions_map.items():
        file.write('{}\t{}\n'.format(k, v))
    file.flush()
    file.close

cursor.close()
connection.close()
