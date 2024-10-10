class University:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
        self.section = []
        
    def dis(self):
        print(f"{self.name}")
        
    def add_student(self,student):
        self.students.append(student)
    
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    
    def add_section(self,section):
        self.section.append(section)
        
    def display(self):
        print(f"Total sections: {len(self.section)}")
        for section in self.section:
            section.display_section_info()
    
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        

class Student(Human):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    
    

class Teacher(Human):
    def __init__(self,name,age,teacher_id):
        super().__init__(name,age)
        self.teacher_id = teacher_id



class Section:
    def __init__(self,section_name,teacher,students,timing):
        self.section_name = section_name
        self.teacher = teacher
        self.students = students
        self.timing = timing
    
    def display_section_info(self):
        print(f"Section Name: {self.section_name}")
        print(f"Timing: {self.timing}")
        print(f"Teacher Name: {self.teacher.name} (ID: {self.teacher.teacher_id})")
        for student in self.students:
            print(f" - {student.name} ID: {student.student_id}")



university = University("University System")


student1 = Student("Ali",21,1)
student2 = Student("Hamza",20,2)
student3 = Student("Umair",22,3)
student4 = Student("Umer",25,4)
student5 = Student("Zahid",23,5)
student6 = Student("Zubair",21,6)
student7 = Student("Laiba",20,7)
student8 = Student("Shazed",26,8)
student9 = Student("Jamshed",23,9)


university.add_student(student1)
university.add_student(student2)
university.add_student(student3)
university.add_student(student4)
university.add_student(student5)
university.add_student(student6)
university.add_student(student7)
university.add_student(student8)
university.add_student(student9)


        
teacher1 = Teacher("Mahmood",45,10)
teacher2 = Teacher("Saba",42,20)
teacher3 = Teacher("Zafar",40,30)


university.add_teacher(teacher1)
university.add_teacher(teacher2)
university.add_teacher(teacher3)
        
        
section1 = Section("English",teacher1,[student1,student2,student3],"9:00AM - 11:00AM")
section2 = Section("Math",teacher2,[student4,student5,student6],"12:00PM - 2:00PM")
section3 = Section("AI",teacher3,[student7,student8,student9],"3:00PM - 5:00PM")


university.add_section(section1)
university.add_section(section2)
university.add_section(section3)

university.dis()
university.display()


