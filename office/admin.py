from django.contrib import admin
from .models import Employee,Project,Requirement,Skill
# Register your models here.
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Requirement)
admin.site.register(Skill)
