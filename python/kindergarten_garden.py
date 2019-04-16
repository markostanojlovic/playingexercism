from collections import defaultdict

PLANTS = {"V":"Violets", "C":"Clover", "R":"Radishes", "G":"Grass"}
STUDENTS = [ "Alice", "Bob", "Charlie", "David",
"Eve", "Fred", "Ginny", "Harriet",
"Ileana", "Joseph", "Kincaid", "Larry"]

class Garden(object):
    def __init__(self, diagram, students=None):
        self.mapping = defaultdict(str)
        for idx, name in enumerate(sorted(students or STUDENTS)):
            for row in diagram.split():
                self.mapping[name] += row[idx*2:(idx+1)*2]

    def plants(self, student):
        return [ PLANTS[plant] for plant in self.mapping[student] ]
