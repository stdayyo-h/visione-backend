from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Project,Requirement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer,SkillSerializer,ProjectSerializer
from .models import Skill,Project
import json
# Create your views here.

class EmployeeView(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serialized=EmployeeSerializer(employees,many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)
    def post(self,request):
        employee_name=request.POST['employee_name']
        email=request.POST['email']
        employee=Employee(employee_name=employee_name, email=email)
        employee.save()
    
    


class RecommendedEmployeesView(APIView):
    def get(self,request):
        return HttpResponse("<h1>NO get Al</h1>",status=status.HTTP_200_OK)
    def post(self,request):
        skills=json.loads(request.body)['skills']
        skills=skills.split(',');
        print(skills)
        employees=Employee.objects.all()
        suitable_employee=[]
        for i in employees:
            for j in i.skills.all():
                if(j.skill_name.split('-')[0]+"-"+j.skill_name.split('-')[1] in skills):
                    print(j.skill_name.split('-')[0]+"-"+j.skill_name.split('-')[1])
                    suitable_employee.append(i)
        serialized=EmployeeSerializer(suitable_employee,many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)

            



class SkillView(APIView):
    def get(self,request):
        skills=Skill.objects.all()
        serialized=SkillSerializer(skills,many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)
    def post(self,request):
        skill_name=request.POST['skill_name']
        skill=Employee(skill_name=skill_name)
        skill.save()
        


class ProjectView(APIView):
    def get(self,request):
        projects=Project.objects.all()
        serialized=ProjectSerializer(projects,many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)
    def put(self,request):
        id=request.POST['id']
        project=Project.objects.get(id=id)
        skills=request.POST['skills'].split(',')
        requirements=[] 
        for i in skills:
            print(i)
            requirements.append(Skill.objects.get(skill_name=i))
        project.project_requirements.set(requirements)
        project.save()
        return Response(ProjectSerializer(project).data,status=status.HTTP_202_ACCEPTED)




        


