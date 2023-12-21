from django.db import models
from django.core.validators import validate_email


class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.university}"
    

class StudyPlan(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='study_plans')
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    
class Equivalence(models.Model):
    destination_university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='equivalences_destination')
    destination_program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='equivalences_destination_program')
    destination_name = models.CharField(max_length=255)
    destination_course_code = models.CharField(max_length=50)
    origin_university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='equivalences_origin')
    origin_course_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.destination_university} - {self.destination_course_code} - {self.destination_name}"
   
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(validators=[validate_email])