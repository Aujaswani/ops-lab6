#!/usr/bin/env python3
# Author ID: Aujaswani

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        """ Return student's name and number in the correct format """
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    def addGrade(self, course, grade):
        """ Add a course and grade to the student's record """
        self.courses[course] = grade

    def displayGPA(self):
        """ Calculate and return the GPA formatted to **one** decimal place """
        gpa = 0.0
        for course in self.courses.keys():
            gpa += self.courses[course]

        if len(self.courses) > 0:
            total_gpa = gpa / len(self.courses)
        else:
            total_gpa = 0.0
        
        return f'GPA of student {self.name} is {total_gpa:.1f}'  # Ensures 1 decimal place

    def displayCourses(self):
        """ Return a list of courses with their grades (only passed courses) """
        passed_course_codes = [course_code for course_code in self.courses.keys() if self.courses[course_code] > 0]
        return passed_course_codes


if __name__ == '__main__':
    # Create the first student object and add grades
    student1 = Student('John', '013345900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops235', 2.0)
    student1.addGrade('ops335', 3.0)

    # Create the second student object and add grades
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('ops245', 3.5)
    student2.addGrade('cpp234', 3.0)

    # Display information for student1
    print(student1.displayStudent())
    print(student1.displayGPA())