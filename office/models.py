from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Skill(models.Model):
    skill_name=models.CharField(max_length=200,null=True,blank=True)
    skill_experience_level=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.skill_name


class Project(models.Model):
    project_name=models.CharField(max_length=200,null=True,blank=True)
    project_requirements=models.ManyToManyField(Skill,blank=True)
    def __str__(self):
        return self.project_name

class Requirement(models.Model):
    skill=models.ManyToManyField(Skill)
    REQUIREMENTS_CHOICES = ((1,"NOT_COMPLETED"),(2, "on_going"),(3, "is_completed"))
    status=models.CharField(REQUIREMENTS_CHOICES,max_length=100,blank=False,null=True)
    def __str__(self):
        return "req"

class Employee(models.Model):
    employee_name=models.CharField(max_length=200,null=True,blank=True)
    emp_image=models.URLField(max_length=200,blank=True,null=True)
    skills=models.ManyToManyField(Skill,blank=True)
    current_projects=models.ManyToManyField(Project,blank=True)
    email=models.CharField(max_length=100,null=True,default="employee@email.com")
    def __str__(self):
        return self.employee_name
