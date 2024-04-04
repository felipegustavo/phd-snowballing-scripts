import database
from lxml import etree

DATASET_FILE = '../dataset/PostLinks.xml'

connection = database.connect()
cursor = connection.cursor()

tree = etree.parse(DATASET_FILE)
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
cursor.close()
connection.close()
