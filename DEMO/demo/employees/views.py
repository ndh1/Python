from django.shortcuts import render
from .models import employees as employee_model
from home.models import department as department_model

# Create your views here.
def get_employees(request, id):
    employee_list = employee_model.objects.filter(department_id=id)
    # employee_model.objects.filter() == Select * from Employees Where department_id = giá trị của id
    department = department_model.objects.get(department_id=id)
    return render(request,'employees.html',{'employee_list':employee_list,'department':department})
    # Đưa dữ liệu của employee_list lên employees.html bằng câu {'department_list': department_list}
