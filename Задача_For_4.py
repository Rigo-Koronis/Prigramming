'''For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.'''
A = int(input('Введите,сколько стоят 1 кг конфет: '))
for i in range(1,11):
    print('{} кг конфет стоит {} р.'.format(i, i*A))