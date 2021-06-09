class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Employee(Human):

    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary

    def get_paid(self):
        return self.salary


class Programmer(Employee):

    def __init__(self, name, surname, salary, bonus):
        super().__init__(name, surname, salary)
        self.bonus = bonus

    def get_paid(self):
        return super().get_paid() + self.bonus


class Manager(Employee):

    def __init__(self, name, surname, salary, multiplication_k):
        super().__init__(name, surname, salary)
        self.multiplication_k = multiplication_k

    def get_paid(self):
        return super().get_paid() * self.multiplication_k


employees = [Programmer('Anton', 'Martynov', 1000, 100),
             Manager('Kyrylo', 'Kozhemyaka', 2000, 1.2),
             Employee('Sam', 'Smith', 800)]

for e in employees:
    print(f"{e} have to be paid: {e.get_paid()}")
