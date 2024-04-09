def write_file_as_csv(filepath, questions_map):
    sorted_questions = dict(sorted(questions_map.items(), key=lambda x: x[1], reverse=True))

    with open(filepath, 'w') as file:
        result = []
        result.append('question id,hits')

        for k, v in sorted_questions.items():
            result.append('{},{}'.format(k, v))

        file.write('\n'.join(result))

        file.flush()
        file.close()