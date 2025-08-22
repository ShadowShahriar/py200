class Employee:
    def __init__(self, name, salary) -> None:
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary


emp = Employee("Shahriar", 75000)
print(f"{emp.get_salary() = :,}")
