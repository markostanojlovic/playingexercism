PLANTS = {"V":"Violets", "C":"Clover", "R":"Radishes", "G":"Grass"}
STUDENTS = [ "Alice", "Bob", "Charlie", "David",
"Eve", "Fred", "Ginny", "Harriet",
"Ileana", "Joseph", "Kincaid", "Larry"]

class Garden(object):
    def __init__(self, diagram, students=None):
        rows = diagram.split()
        students = sorted(students or STUDENTS)
        self.mapping = {}
        for student in range(len(rows[0]) // 2):
            student_name = students.pop(0)
            for row in rows:
                if student_name in self.mapping:
                    self.mapping[student_name] += row[student*2:(student+1)*2]
                else:
                    self.mapping[student_name] = row[student*2:(student+1)*2]

    def plants(self, student):
        return [ PLANTS[plant] for plant in self.mapping[student] ]
