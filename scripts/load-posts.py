import database
from lxml import etree

DATASET_FILE = '../dataset/Posts.xml'

connection = database.connect()
cursor = connection.cursor()

tree = etree.parse(DATASET_FILE)
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
     attrs['Score'], attrs.get('ViewCount', None), attrs['Body'],
     attrs.get('OwnerUserId', None), attrs.get('LastActivityDate', None),
     attrs.get('Title', None), attrs.get('Tags', None), attrs.get('AnswerCount', None),
     attrs['CommentCount'], attrs.get('ContentLicense', None)])
    print("Post {} inserido".format(attrs['Id']))

connection.commit()
cursor.close()
connection.close()
