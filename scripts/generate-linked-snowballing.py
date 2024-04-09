from utils import database
from utils import files

op = input('1 - Backward; 2 - Forward: ')

if (op == '1'):
    output = 'out/ids_linked_links_backward_snowballing.csv'
    query = '''
    select pl.related_post_id  from post_link pl
    where
        pl.link_type_id = 1 and
        pl.post_id in (select distinct ps1.id from post_startset ps1) and
        pl.related_post_id not in (select ps2.id from post_startset ps2)
        order by pl.creation_date desc
    '''

else:
    output = 'out/ids_linked_links_forward_snowballing.csv'
    query = '''
    select pl.post_id from post_link pl
    where
        pl.link_type_id  = 1 and
        pl.post_id not in (select ps1.id from post_startset ps1) and
        pl.related_post_id in (select ps2.id from post_startset ps2)
    order by pl.creation_date  desc
    '''

connection = database.connect()
cursor = connection.cursor()

cursor.execute(query)
rows_post = cursor.fetchall()

questions_map = dict()

for row in rows_post:
    id = row[0]
    questions_map[id] = questions_map.get(id, 0) + 1

files.write_file_as_csv(output, questions_map)

cursor.close()
connection.close()
