from django.urls import path
from . import views
urlpatterns=[
    path('employees',views.EmployeeView.as_view(),name="employee"),
    path('skills',views.SkillView.as_view(),name="skills"),
    path('projects',views.ProjectView.as_view(),name="projects"),
    path('recommended',views.RecommendedEmployeesView.as_view(),name="recommended employees")

]