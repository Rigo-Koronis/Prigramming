import json

filename = 'students.json'
with open(filename) as f:
    students_new = json.load(f)

max_score_exam = []
max_score_quiz = []
max_score_homework = []
all_students =[]

i = 0
while i < 200 :

    students_new0 = students_new[i]

    students_new00 = students_new0['scores']
    students_new000 = students_new00[0]

    students_new0000 = students_new00[0]

    students_new0001 = students_new00[1]

    students_new0002 = students_new00[2]

    max_score_exam.append(students_new0000['score'])
    max_score_quiz.append(students_new0001['score'])
    max_score_homework.append(students_new0002['score'])

    all_students.append(students_new0['name'])
    i += 1

max(max_score_exam)

max_score_exam.index(max(max_score_exam))

max(max_score_quiz)

max_score_quiz.index(max(max_score_quiz))

max(max_score_homework)

max_score_homework.index(max(max_score_homework))

print('Студент набравший максимальный балл за exam :', all_students[max_score_exam.index(max(max_score_exam))],'. Он набрал', max(max_score_exam), 'баллов.')
print('Студент набравший максимальный балл за quiz :', all_students[max_score_quiz.index(max(max_score_quiz))],'. Он набрал', max(max_score_quiz), 'баллов.')
print('Студент набравший максимальный балл за homework :', all_students[max_score_homework.index(max(max_score_homework))], '. Он набрал', max(max_score_homework), 'баллов.')
