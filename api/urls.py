from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    path('employees/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]
