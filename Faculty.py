class Faculty:
    def __init__(self, name, subject, mobilenumber, salary):
        self.name = name
        self.subject = subject
        self.mobilenumber = mobilenumber
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Mobile:", self.mobilenumber)
        print("Salary:", self.salary)


class Science_Faculty(Faculty):
    def __init__(self, name, subject, mobilenumber, salary, lab_time):
        super().__init__(name, subject, mobilenumber, salary)
        self.lab_time = lab_time

    def display(self):
        super().display()
        print("Lab Time:", self.lab_time)
        print("----------------------")


f1 = Faculty("Valentino", "Physics", 9876543210, 45000)
s1 = Science_Faculty("Marc", "Aerodynamics", 9123456780, 55000, "2 PM - 4 PM")

f1.display()
print("----------------------")
s1.display()