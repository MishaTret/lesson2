#class Student:
    #amount_of_students = 0
    #group = "S 2929"
    #height = 150
    #def __init__(self, height = 160):
        #self.height = height
        #Student.amount_of_students += 1

#st1 = Student()
#st2 = Student()
#st3 = Student()
#st4  =Student()
#print(st1.height)
#print(st2.height)
#print(Student.amount_of_students)

#class Student:
    #height = 150
#    def __init__(self):
#        print(self.height)
 #       self.height += 20

#st1 = Student()
#st2 = Student()

class Student:
    amount_of_students = 0

    def __init__(self, height = 160):
        self.height = height
        Student.amount_of_students += 1

    def grow(self, height=1):
        self.height += height

nick = Student()
kate = Student(height=175)
nick.grow(height=25)

print(nick.height)
print(kate.height)