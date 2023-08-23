import student
import course
import department

def main() -> None:
    print("!Department_run!")
    s_list = [student.Student(f"name{i}") for i in range(2)]
    c_list = [course.Course("course_name", 15, s_list) for i in range(10)]
    d = department.Department(c_list)
    print('---select_courses---')
    arr = d.courses
    for item in arr:
        print(item)
    print('---set_courses---')
    s_list = [student.Student(f"name_1{i}") for i in range(2)]

    c_list = [course.Course("course_name", 16, s_list) for i in range(10)]
    d = department.Department(c_list)
    arr = d.courses
    for item in arr:
        print(item)

if __name__ == "__main__":
    main()
