# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных
# # чисел ичисел больше 100 тысяч.

while True:
    number = int(input('Введите положтельное число: '))
    if number > 0:
        break

if number == 1 or number == 2:
    print('Число простое.')
is_simple = False
for i in range(2, number):
    if number % i == 0:
        print('Число составное.')
        break
    else:
        is_simple = True
if is_simple:
    print('Число простое.')

