import student
import course
import copy
from typing import List, Type

course_list_type = List[course.Course]

class Department:
    def __init__(self, courses: course_list_type) -> None:
        self._cources = courses

    @property
    def courses(self) -> course_list_type:
        return copy.deepcopy(self._cources)

    @courses.setter
    def courses(self, set_courses: course_list_type) -> None:
        self._cources = set_courses

def main() -> None:
    print("!Department_run!")
    s_list = [student.Student(f"name{i}") for i in range(2)]
    c_list = [course.Course("course_name", 15, s_list) for i in range(10)]
    d = Department(c_list)
    print('---select_courses---')
    arr = d.courses
    for item in arr:
        print(item)
    print('---set_courses---')
    s_list = [student.Student(f"name_1{i}") for i in range(2)]

    c_list = [course.Course("course_name", 16, s_list) for i in range(10)]
    arr = d.courses
    for item in arr:
        print(item)

if __name__ == "__main__":
    main()
