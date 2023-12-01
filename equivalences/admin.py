from django.contrib import admin
from .models import University, Program, Section, Course, RecognizedCourse

# Register your models here.
admin.site.register(University)
admin.site.register(Program)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(RecognizedCourse)
