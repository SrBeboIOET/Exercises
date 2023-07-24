students = {}

while True:
    name_student = input("Enter the name of student (or 'exit' for finish): ")
    if name_student.lower() == "exit":
        break
    grades = []
    for i in range(3):
        nota = float(input(f"Enter de grade {i+1} from student: "))
        grades.append(nota)
    students[name_student] = {"grades": grades}
    students[name_student] = {"grades": grades, "average": sum(grades)/len(grades)}

print("Student's grades:")
for student in students:
    print(f"{student}: {students[student]['grades']}")
print()

print("General average from course:")
for student in students:
    print(f"{student}: {students[student]['average']}")
print()

general_average = sum([students[student]['average'] for student in students])/len(students)
print(f"General average from course: {general_average}")
