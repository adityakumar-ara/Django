from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True) # Roll number unique hona chahiye
    phone_number = models.CharField(max_length=15)
    village_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
