class Candidate:
    def __init__(self, name, age, qualification, experience):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.experience = experience

    def introduce_yourself(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Qualification:", self.qualification)
        print("Experience:", self.experience)
        print("----------------------")


c1 = Candidate("Arjun", 22, "B.Tech", "4 Years")
c2 = Candidate("Rossi", 25, "B.Tech", "4 Years")
c3 = Candidate("Marc", 24, "BBA", "3 Years")

c1.introduce_yourself()
c2.introduce_yourself()
c3.introduce_yourself()

del c1.age

del c1