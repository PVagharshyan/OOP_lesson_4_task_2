class Student:
    _id: int = 0
    def __init__(self, name: str) -> None:
        self._name = name
        self._current_id = Student._id
        Student._id += 1

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, set_name: str) -> None:
        self._name = set_name

    @property
    def id(self) -> int:
        return self._current_id

def main():
    print("!student_run!")
    s = Student("Petros")
    print('----select_name----')
    print(s.name)
    print('----set_name-----')
    s.name = "Poxos"
    print(s.name)
    print('---select_id---')
    print(s.id)

if __name__ == "__main__":
    main()

