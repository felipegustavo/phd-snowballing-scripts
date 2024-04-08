def write_file_as_csv(filepath, questions_map):
    sorted_questions = dict(sorted(questions_map.items(), key=lambda x: x[1], reverse=True))
    with open(filepath, 'w') as file:
        file.write('question_id\thits\n')
        for k, v in sorted_questions.items():
            file.write('{},{}\n'.format(k, v))
        file.flush()
        file.close()