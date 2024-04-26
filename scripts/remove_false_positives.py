from utils import database

connection = database.connect()
cursor = connection.cursor()

cursor.execute('select * from post_false_positive')
false_positives = set(temp_row[0] for temp_row in cursor.fetchall())

csv_list = [
    'out/LINKED BS.csv',
    'out/LINKED FS.csv',
    'out/RELATED BS.csv',
    'out/RELATED FS.csv',
    'out/Duplicações.csv'
]

for csv in csv_list:
    output = []
    with open(csv, 'r') as file:
        header = file.readline().replace('\n', '')
        output.append(header)
        for line in file:
            line = line.replace('\n', '')
            id = int(line.split(',')[0])
            if id not in false_positives:
                output.append(line)

    with open(csv, 'w') as file:
        file.write('\n'.join(output))
        file.close()
