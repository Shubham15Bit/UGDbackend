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
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='study_plan')
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    
class Subject(models.Model):
    study_plans = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name