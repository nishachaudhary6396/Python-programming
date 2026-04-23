class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"{self.name} and {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        super().display()
        print(self.department)
class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language

    def show_language(self):
        print(self.language)

man = Manager("Nisha","50k","SDE")
dev = Developer("Nisha","50k","Python")
man.display()
dev.display()
dev.show_language()
