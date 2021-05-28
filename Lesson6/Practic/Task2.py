from collections import Counter

first_task = []
second_task = []
third_task = []
strk = []

Python = ['Иван Иванов', 'Петр Петров', 'Сидор Сидоров', 'Роман Басов']
FrontEnd = ['Виктор Цой', 'Сергей Зайцев', 'Сидор Сидоров', 'Юрий Хой']
FullStack = ['Дмитрий Запара', 'Петр Петров', 'Макс Молотков', 'Юрий Гурьев']
Java = ['Сергей Зверев', 'Дмитрий Князев', 'Василий Васечкин']

strk = Python + FrontEnd + FullStack + Java

c = Counter(list(map(lambda x: x, strk)))
for name, count in c.items():
    if count > 1:
        first_task.append(name)

print('Студенты, которые учатся в двух и более группах -', first_task)

second_task = set(strk) | set(FrontEnd)

print()
print('Студенты, которые не учатся на фронтенде -', list(second_task))
print()
print('Студенты изучающие Python- ', Python)
print()
print('Студенты изучающие Java- ', Java)
