'''For9. Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.'''
A = int(input('Введите число A: '))
B = int(input('Введите число B, которое больше числа A: '))
C = A*A
if A < B:
    for i in range(A+1, B+1,):
        C = C + i * i
    print(' Сумма квадратов всех чисел, от {} до {} включительно, равна {} ' .format(A, B, C))
elif A > B:
    print('Вы ввели число B={}, которое больше, чем число A={}. Пожалуйста введите число B, которое будет больше числа A '.format(A, B))
else:
    print('Вы ввели число B={}, равное числу A={}. Пожалуйста введите число B, которое будет больше числа A '.format(A, B))