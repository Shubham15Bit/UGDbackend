from django.contrib import admin
from .models import University, Program, StudyPlan, Equivalence

# Register your models here.
admin.site.register(University)
admin.site.register(Program)
admin.site.register(StudyPlan)
admin.site.register(Equivalence)
