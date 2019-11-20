import json

filename = 'students.json'
with open(filename) as f:
    students_new = json.load(f)

all_score_exam = []
all_score_quiz = []
all_score_homework = []
all_students =[]

for student_i in students_new:
    student_i = students_new[student_i['_id']]

    student_scores = student_i['scores']

    exam = student_scores[0]
    quiz = student_scores[1]
    homework = student_scores[2]

    all_score_exam.append(exam['score'])
    all_score_quiz.append(quiz['score'])
    all_score_homework.append(homework['score'])
    all_students.append(student_i['name'])

max(all_score_exam)
all_score_exam.index(max(all_score_exam))

max(all_score_quiz)
all_score_quiz.index(max(all_score_quiz))

max(all_score_homework)
all_score_homework.index(max(all_score_homework))

print('Студент набравший максимальный балл за exam :', all_students[all_score_exam.index(max(all_score_exam))],'. Он набрал', max(all_score_exam), 'баллов.')
print('Студент набравший максимальный балл за quiz :', all_students[all_score_quiz.index(max(all_score_quiz))],'. Он набрал', max(all_score_quiz), 'баллов.')
print('Студент набравший максимальный балл за homework :', all_students[all_score_homework.index(max(all_score_homework))], '. Он набрал', max(all_score_homework), 'баллов.')