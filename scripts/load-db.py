from utils import database
from lxml import etree
from utils import database

import stackapi
import json

def load_startset():
    with open('dataset/startset.txt', 'r') as file:
        for line in file:
            cursor.execute('INSERT INTO public.post_startset(id) VALUES(%s)', [line.strip()])

    connection.commit()

def load_posts():
    tree = etree.parse('dataset/Posts.xml')
    root = tree.getroot()

    for child in root:
        attrs = child.attrib
        cursor.execute(
        '''
            INSERT INTO public.post(id, post_type_id, creation_date, score,
                view_count, body, owner_user_id, last_activity_date, title,
                tags, answer_count, comment_count, content_license)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''',
        [attrs['Id'], attrs['PostTypeId'], attrs['CreationDate'],
        attrs['Score'], attrs.get('ViewCount'), attrs['Body'],
        attrs.get('OwnerUserId'), attrs.get('LastActivityDate'),
        attrs.get('Title'), attrs.get('Tags'), attrs.get('AnswerCount'),
        attrs['CommentCount'], attrs.get('ContentLicense')])
        print("Post {} inserido".format(attrs['Id']))
        
    connection.commit()

def load_posts_links():
    tree = etree.parse('dataset/PostLinks.xml')
    root = tree.getroot()

    for child in root:
        attrs = child.attrib
        cursor.execute(
        '''
            INSERT INTO public.post_link(id, creation_date, post_id, related_post_id, link_type_id)
            VALUES(%s, %s, %s, %s, %s)
        ''',
        [attrs['Id'], attrs['CreationDate'], attrs['PostId'], attrs['RelatedPostId'], attrs['LinkTypeId']])
        print("Post Link {} inserido".format(attrs['Id']))

    connection.commit()

def load_related_posts():
    try:
        site = stackapi.StackAPI(name='pm', key='PuwVddLxBbyPkjEP5SyzYQ((')
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
            print('Links related do post {} inseridos no banco'.format(post_id))
        
        print('Posts inseridos com sucesso. Ultimo post inserido: {}'.format(post_id))
    except RuntimeError as err:
        print('Houve um erro: {}'.format(err))
    finally:
        connection.commit()
        print("Acabou, terminei no id {}".format(post_id))

op = input('1 - startset; 2 - posts; 3 - posts links; 4 - related posts: ')

funcs = {
    '1': load_startset,
    '2': load_posts,
    '3': load_posts_links,
    '4': load_related_posts
}

connection = database.connect()
cursor = connection.cursor()

funcs[op]()

cursor.close()
connection.close()
