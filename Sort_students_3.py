import json

filename = 'students.json'
with open(filename) as f:
    students_new = json.load(f)

all_score_exam = []
all_score_quiz = []
all_score_homework = []
all_students = []

for student_i in students_new:
    student_scores = student_i['scores']

    for student_scores_i in student_scores:
        type_score = student_scores_i['score']

        if student_scores_i['type'] == 'exam':
            all_score_exam.append(type_score)
        elif student_scores_i['type'] == 'quiz':
            all_score_quiz.append(type_score)
        elif student_scores_i['type'] == 'homework':
            all_score_homework.append(type_score)

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