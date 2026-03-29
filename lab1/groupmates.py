groupmates = [
    {
        "name": "Арина",
        "group": "2256",
        "age": 24,
        "marks": [4, 5, 5, 5, 4]
    },
    {
        "name": "Оксана",
        "group": "2256",
        "age": 23,
        "marks": [5, 5, 5, 4, 5]
    },
    {
        "name": "Алена",
        "group": "2256",
        "age": 25,
        "marks": [5, 5, 4, 3, 5]
    },
    {
        "name": "Алексей",
        "group": "2256",
        "age": 22,
        "marks": [5, 3, 5, 4, 5]
    }
]

def print_students(students):
    print(f"{'Имя студента':<15} {'Группа':<8} {'Возраст':<8} {'Оценки':<20}")
    for student in students:
        print(f"{student['name']:<15} {student['group']:<8} {student['age']:<8} {str(student['marks']):<20}")
    print()

print_students(groupmates)

def middle_mark (students, min_avg):
    result = []
    for student in students:
        marks = student["marks"]
        avg = sum(marks) / len(marks) #считаем средний балл

        if avg > min_avg:
            result.append(student)

    return result
    
filtered_students = middle_mark(groupmates, 4.5) #средняя оценка сравнивается с 4.5
print_students(filtered_students)