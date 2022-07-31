from django.shortcuts import render
from .models import department as department_model
# Create your views here.
def get_home(request):
    department_list = department_model.objects.filter().order_by('department_id')
    # department_model.objects.filter() == Select * from Department
    return render(request,'home.html',{'department_list': department_list})
    # Đưa dữ liệu của department_list lên home.html bằng câu {'department_list': department_list}


