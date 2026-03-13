class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print("Sinh viên", self.name, "có điểm là", self.score)

s1 = Student("A", 10)
s1.display()