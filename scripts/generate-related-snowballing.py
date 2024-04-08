from utils import database
from utils import files

import json

def is_valid_question_bs(question):
    return question['score'] >= 8 and question['answer_count'] >= 4


op = input('1 - Backward; 2 - Forward: ')

if (op == '1'):
    output = 'out/ids_related_links_backward_snowballing.csv'
    query = '''
    select * from post_link_related
    where post_id in (select id from post_startset)
    '''

else:
    output = 'out/ids_related_links_forward_snowballing.csv'
    query = '''
    select * from post_link_related
    where
	    post_id not in (select id from post_startset) and
	    post_id in (select id from post where answer_count >= 4 and score >= 8)
    '''

connection = database.connect()
cursor = connection.cursor()

cursor.execute(query)
rows = cursor.fetchall()

questions_map = dict()

if op == '1':

    # Iterando por discussões relacionadas apontadas pelo startset
    for row in rows:
        data = json.loads(row[1]) # parseando response body
        items = data['items']
        for item in items:
            if is_valid_question_bs(item):
                related_id = item['question_id']
                questions_map[related_id] = questions_map.get(related_id, 0) + 1

elif op == '2':

    # Iterando por discussões para achar qual aponta para o starset
    cursor.execute('select id from post_startset')
    startset = set(temp_row[0] for temp_row in cursor.fetchall())

    for row in rows:
        data = json.loads(row[1])
        items = data['items']
        parent_id = row[0]

        for item in items:
            related_id = item['question_id']
            # checo se o post tem algum post relacionado que bate com o startset
            if related_id in startset:
                questions_map[parent_id] = questions_map.get(parent_id, 0) + 1
            
files.write_file_as_csv(output, questions_map)

cursor.close()
connection.close()