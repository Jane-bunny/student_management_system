# Define Student class as blueprint for new object

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Course:
    def __init__(self, name):
        self.name = name
        self.students = StudentRegister()

    def add_student(self, new_student):
        self.students.add(new_student.name, new_student.number)

    def remove_student(self, student):
        self.students.delete(student.name,student.number)
    

class StudentRegister:
    def __init__(self):
        self.list = []
   

    def add(self, name, number):
        if not self.exists(name, number):
            self.list.append(Student(name, number))

    def delete(self, name, number):
        for item in self.list:
            if item.name == name and item.number == number:
                self.list.remove(item)

    def exists(self, name, number):
        result = False
        for item in self.list:
            if item.name == name and item.number == number:
                result = True
        return result   
    
    def find_student(self, name, number) -> Student:
        if self.exists(name, number):
            for item in self.list:
                if item.name == name and item.number == number:
                    result = item
        return item

    def return_register(self):
        return self.list
    

class CourseRegister:
    def __init__(self, name):
        self.list = []
        self.name = name

    def add(self, name):
        if not self.exists(name):
            self.list.append(Course(name))

    def delete(self, name):
        for item in self.list:
            if item.name == name:
                self.list.remove(item)

    def exists(self, name):
        result = False
        for item in self.list:
            if item.name == name:
                result = True
        return result
    
    def find_course(self, name) -> Course:
        if self.exists(name):
            for item in self.list:
                if item.name == name:
                    result = item
        return item

    def return_register(self):
        return self.list