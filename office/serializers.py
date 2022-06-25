from rest_framework.serializers import ModelSerializer
from .models import Employee,Skill,Project

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"


class SkillSerializer(ModelSerializer):
    class Meta:
        model=Skill
        fields="__all__"

class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"