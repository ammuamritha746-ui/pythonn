a = """Python Full Stack Development Course
provides comprehensive training in Python programming, front-end and back-end development, databases, and web application development. The course helps students build dynamic and responsive web applications using modern technologies and gain 
practical skills through real-world projects"""
print(len(a))
print(a[:51])
print(a.replace("python","PYTHON"))
print(a.upper())
print(a.strip())
words = a.split()
print(words)
if "course" in words:
  print("the word 'course' exists in the paragragh.")
  print("the course is {} characters long and has {} words".format(len(a), len(words)))