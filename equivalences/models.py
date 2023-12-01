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

class Section(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.program}"

class Course(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    prerequisites = models.CharField(max_length=200, blank=True, null=True)
    weekly_hours = models.IntegerField(blank=True, null=True)
    total_hours = models.IntegerField(blank=True, null=True)
    term = models.CharField(max_length=20, blank=True, null=True)
    teaching_mode = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class RecognizedCourse(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='recognized_courses')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='recognized_courses')
    code = models.CharField(max_length=10, blank=True, null=True)
    ugd_subject = models.CharField(max_length=200, blank=True, null=True)
    unl_recognized_subject = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.original_course} - {self.unl_recognized_subject}"
