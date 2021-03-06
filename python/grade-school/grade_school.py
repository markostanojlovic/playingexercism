from collections import defaultdict
from itertools import chain

class School(object):
    def __init__(self):
        self.school = defaultdict(list)

    def add_student(self, name, grade):
        self.school[grade].append(name)

    def grade(self, grade_number):
        return sorted(self.school[grade_number])

    def roster(self):
        return list(chain.from_iterable([self.grade(grade_num) for grade_num in sorted(self.school.keys())]))
