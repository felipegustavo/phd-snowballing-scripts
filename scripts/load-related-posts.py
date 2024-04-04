import database
import stackapi
import json

connection = database.connect()

try:
    site = stackapi.StackAPI(name='pm', key='PuwVddLxBbyPkjEP5SyzYQ((')

    cursor = connection.cursor()
    cursor.execute('''
                select id  from post
                where
	                id not in (select post_id from post_link_related) and
	                post_type_id = 1
                order by creation_date desc''')
    rows_post = cursor.fetchall()

    for row_post in rows_post:
        post_id = row_post[0]
        print('Consultando links related do post {}'.format(post_id))
        posts_stack = site.fetch('questions/{ids}/related', sort='activity', order='desc', ids=[post_id])
        json_string = json.dumps(posts_stack)
        cursor.execute('insert into post_link_related(post_id, response_body) VALUES(%s, %s)', [post_id, json_string])
        connection.commit()
        print('Links related do post {} inseridos no banco'.format(post_id))
        
    cursor.close()
    print('Posts inseridos com sucesso. Ultimo post inserido: {}'.format(post_id))
except RuntimeError as err:
    print('Houve um erro: {}'.format(err))
finally:
    print("Acabou, terminei no id {}".format(post_id))
    connection.commit()
    connection.close()
