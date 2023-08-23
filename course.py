import student
import copy
from typing import List, Type

student_list = List[student.Student]

class Course:
    def __init__(self, course_name: str, credits: int, students: student_list = []) -> None:
        self._course_name = course_name
        self._credits = credits
        self._students = students

    def __str__(self) -> str:
        str_students = [f" {self._students[i]}, " if (i != len(self._students) - 1) \
                        else f" {self._students[i]} " \
                        for i in range(len(self._students))]
        str_students = ''.join(str_students)
        return f"students: {str_students}, \ncourse_name: {self.course_name}, credits: {self.credits}"

    def join_student(self, current_student: student.Student) -> None:
        if current_student in self._students:
            print(f"Error: this {current_student} student already exists")
            return
        self._students.append(current_student)

    @property
    def course_name(self) -> str:
        return self._course_name

    @course_name.setter
    def course_name(self, set_course_name: str) -> None:
        self._course_name = set_course_name

    @property
    def credits(self) -> int:
        return self._credits

    @credits.setter
    def credits(self, set_credits: int) -> None:
        if (set_credits <= 0):
            raise ValueError(f"Error: credit cannot be negative or 0")
        self._credits = set_credits

    @property
    def students(self) -> student_list:
        return copy.deepcopy(self._students)

    @students.setter
    def students(self, set_students: student_list) -> None:
        self._students = set_students

def main() -> None:
    print("!cource_run!")
    print('------test-------')
    s_list = [student.Student('name') for i in range(10)]
    c = Course('math', 10, s_list)
    print('---select_course_name---')
    print(c.course_name)
    print('---set_course_name---')
    c.course_name = 'math_1'
    print(c.course_name)
    print('---select_credits---')
    print(c.credits)
    print('---set_credits---')
    c.credits = 20
    print(c.credits)
    print('---select_students---')
    arr = c.students
    for item in arr:
        print(item)
    print('---set_students---')
    s_list = [student.Student('name_1') for i in range(10)]
    c.students = s_list
    arr = c.students
    for item in arr:
        print(item)

if __name__ == "__main__":
    main()
