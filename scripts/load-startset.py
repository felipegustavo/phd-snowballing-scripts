import database

DATASET_FILE = '../dataset/startset.txt'

connection = database.connect()
cursor = connection.cursor()

with open(DATASET_FILE, 'r') as file:
    for line in file:
        cursor.execute('INSERT INTO public.post_startset(id) VALUES(%s)', [line.strip()])

connection.commit()
cursor.close()
connection.close()
