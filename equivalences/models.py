from django.db import models


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
    destination_university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='equivalences_origin')
    destination_program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='equivalences_origin_program')
    destination_name = models.CharField(max_length=255)
    destination_course_code = models.CharField(max_length=50)
    origin_university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='equivalences_destination')
    origin_course_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.destination_university} - {self.destination_course_code} - {self.destination_course_name}"
   
    