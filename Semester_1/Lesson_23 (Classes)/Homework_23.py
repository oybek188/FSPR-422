# https://www.codewars.com/kata/54fe05c4762e2e3047000add

# Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20


# Color Ghost
import random
class Ghost(object):

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])  
ghost = Ghost()


# Refactored Greeting
class Person():
    
    def __init__(self, name):
        self.name = name
    
    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"

# 
class Student: 
    def __init__(self, first_name, last_name, grades=[]): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.grades = list(grades) # [] 
     
    def add_grade(self, grade): 
        self.grades.append(grade) 
     
    def get_average(self): 
        return sum(self.grades) / len(self.grades) 
 
johnDoe = Student('John', 'Doe') 
janeDoe = Student('Jane', 'Doe') 
jamesSmith = Student('James', 'Smith') 
jennaSmith = Student('Jenna', 'Smith') 
students = (johnDoe, janeDoe, jamesSmith, jennaSmith) # tuple 
 
johnDoe = Student('John', 'Doe') 
janeDoe = Student('Jane', 'Doe') 
jamesSmith = Student('James', 'Smith') 
jennaSmith = Student('Jenna', 'Smith') 
students = johnDoe, janeDoe, jamesSmith, jennaSmith 
 
firstAssessmentGrades = [63, 92, 82, 75] 
for i, student in enumerate(students): 
    student.add_grade(firstAssessmentGrades[i]) 
 
for i, student in enumerate(students): 
    print(student.grades[0], firstAssessmentGrades[i])

