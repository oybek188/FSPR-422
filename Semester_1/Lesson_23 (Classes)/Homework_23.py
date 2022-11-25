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