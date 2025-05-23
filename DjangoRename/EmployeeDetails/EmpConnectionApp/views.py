from django.shortcuts import render
from EmpConnectionApp.models import Employee

#
# emp = Employee.objects.all()
# print(emp)

def employee_info_view(request):
    employees = Employee.objects.all()
    return render(request,'EmpConnectionApp/index.html',{'employees':employees})
# Create your views here.
