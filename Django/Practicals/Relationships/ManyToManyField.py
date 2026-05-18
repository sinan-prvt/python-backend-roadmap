# =================================== ManyToManyField



# --------------- Basic Example


## == models.py

# class Student(models.Model):
#     name = models.CharField(max_length=100)

# class Course(models.Model):
#     title = models.CharField(max_length=200)

# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)





# ------------------- Accessing Related Objects


## == models.py

# class Student(models.Model):
#     name = models.CharField(max_length=100)


# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     students = models.ManyToManyField(Student, related_name='courses')



## == views.py
# Accessing the related Courses from a Student instance

# student = Student.objects.get(id=1)
# courses = student.course_set.all()
# for course in courses:
#     print(course.title)





