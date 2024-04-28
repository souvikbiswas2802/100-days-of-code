class job:
  name = None
  salary = None
  hoursWorked = None
  def __init__ (self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked
  def printing(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hoursWorked}\n")

class doctor(job):
  speciality = None
  experience = None
  def __init__ (self, salary, hoursWorked, speciality, experience):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.speciality = speciality
    self.experience = experience
  def printing(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hoursWorked}\nSpeciality: {self.speciality}\nExperience:{self.experience}\n")
  
class teacher(job):
  subject = None
  position = None
  def __init__ (self, salary, hoursWorked, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position
  def printing(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hoursWorked}\nSubject: {self.subject}\nPosition: {self.position}\n")


engineer = job("Engineer", "$100,000", "40")
engineer.printing()

doctor = doctor("$120,000", "48", "Pediatric Consultant", "7")
doctor.printing()

teacher = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teacher.printing()
