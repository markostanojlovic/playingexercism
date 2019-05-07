from collections import defaultdict

class School(object):
    def __init__(self):
        self.school = defaultdict(list)

    def add_student(self, name, grade):
        self.school[grade] += [name]

    def roster(self):
        results = []
        for grade in sorted(self.school.keys()):
            results += sorted(self.school[grade])
        return results

    def grade(self, grade_number):
        return sorted(self.school[grade_number])
