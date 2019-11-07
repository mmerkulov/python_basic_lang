# Part 1
welcom_phrase = 'Hello GeekBrainns'
my_name = 'Merkulov Mikhail'
full_string = welcom_phrase + '! \nMy name is ' + my_name
print(full_string)

# Part 2
main_value = int(input('Введите время в секундах = '))
sec = 0
hour = 0
minuta = 0

if main_value > 60:
    minuta = main_value // 60
    sec = main_value % 60
    if minuta > 60:
        hour = minuta // 60
        minuta = minuta % 60
else:
    sec = main_value

sec = str(sec)
minuta = str(minuta)
hour = str(hour)

if len(sec) != 2:
    sec = '0' + sec
if len(hour) != 2:
    hour = '0' + hour
if len(minuta) != 2:
    minuta = '0' + minuta
full_string = hour + ':' + minuta + ":" + sec
print('Результат = ' + str(full_string))

# Part 3
n = input('Часть 3. Введите число = ')
n2 = n + n
n3 = n + n + n
summ = int(n) + int(n2) + int(n3)
print(str(summ))

# Part 4
value = str(input('Часть 4. Введите число = '))
length = len(value)
i = 0
while i < int(length):
    print('i = ' + str(i))
    if i == length-1:
        break
    if value[i] > value[i + 1]:
        max = value[i]
    else:
        max = value[i + 1]
    i += 1
print('Результат =' + str(max))

# Part 5
print('Часть 5.')
revenue = int(input('Введите значение выручки = '))
cost = int(input ('Введите значение издержек = '))

if revenue > cost:
    print('Поздравляем, у вас прибыль!')
    proceeds = ((revenue - cost) / revenue) * 100
    print('Рентабельность выручки = ' + str(proceeds) + '%')
else:
    print('Сожалеем, у вас убытки!')

amout_staff = int(input('Введите количество сотрудников = '))
x = (revenue - cost) / amout_staff
# print('Соотношение одного сотрудников к прибыли = ' + str(x))

# Part 6
print('Часть 6.')
a = int(input('Количество км = '))
b = int(input('Цель в км = '))
day = 1
while a < b:
    a = a * 0.1 + a
    day +=1

print('Через ' + str(day) + ' дней будет достигнута цель = ' + str(b) + ' км')