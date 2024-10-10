# University system
This is a Python-based University System that manages students, teachers, and sections. It 
demonstrates core Object-Oriented Programming (OOP) concepts such as inheritance,
encapsulation, and polymorphism.

# Classes
1. ***Human***
Attributes: name, age
The base class for both Student and Teacher.
2. ***Student*** (Inherits from Human)
Attributes: student_id (Unique ID for each student)
3. ***Teacher*** (Inherits from Human)
Attributes: teacher_id (Unique ID for each teacher)
4. ***Section***
Attributes: section_name, teacher, students, timing
Methods: display_section_info() — Displays the details of the section (teacher, students, timing).
5. ***University***
Attributes: students, teachers, sections (Lists of all students, teachers, and sections in the university)
Methods:
add_student(student): Adds a student to the university.
add_teacher(teacher): Adds a teacher to the university.
add_section(section): Adds a section to the university.
display_active_sections(): Displays all active sections and their details.
