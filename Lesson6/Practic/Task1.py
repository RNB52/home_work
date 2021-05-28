students = {"Ivanov Ivan": [5, 5, 5], "Petrov Petr": [
    3, 3, 5], "Sidorov Sidr": [5, 5, 5], "Vasechkin Vasya": [3, 2, 3]}
best = list()
worst = list()

for i in students:
    average = sum(students[i]) / len(students[i])
    students[i] = average

max_rating = max(students.values())
min_rating = min(students.values())
# print(max_rating)
# print(min_rating)

for name, rating in students.items():
    if rating == max_rating:
        best.append(name)
    elif rating == min_rating:
        worst.append(name)

print('Лучший студент -', best)
print('Худший студент -', worst)
