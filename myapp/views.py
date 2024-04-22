from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CreateCompanyForm, UpdateCompanyForm, CreateEmployeeForm, UpdateEmployeeForm

# Create your views here.

#render index page
def index(request):
    return render(request,"index.html")


#company list page with search and sorted feature
def company(request):
    company = Company.objects.all()
    sorted = request.GET.get('sort')
    #sort feature
    if sorted:
        company = Company.objects.all().order_by(sorted)
    #search feature
    if request.method == 'GET':
        query = request.GET.get('query','')
        posts = Company.objects.filter(Q(name__icontains=query))
        return render(request, 'company.html', {'query':query,'posts': posts, 'company':company})
    else:
        return render(request,"company.html", context={'company':company})


#employee list page with search and sorted feature added
def employee(request):
    employee = Employee.objects.all()
    sorted = request.GET.get('sort')
    #sort feature
    if sorted:
        employee = Employee.objects.all().order_by(sorted)
    #search feature
    if request.method == 'GET':
        query = request.GET.get('query','')
        posts = Employee.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query))
        return render(request, 'employee.html', {'query':query,'posts': posts, 'employee':employee})
    else:
        return render(request,"employee.html", context={'employee':employee})


#add company view
class CreateCompanyView(LoginRequiredMixin,CreateView):
    model = Company
    template_name = "add_company.html/"
    form_class = CreateCompanyForm
    success_url = reverse_lazy('company')


#update company view
class UpdateCompanyView(LoginRequiredMixin,UpdateView):
    model = Company
    template_name = "update_company.html/"
    form_class = UpdateCompanyForm
    success_url = reverse_lazy('company')


#add employee view
class CreateEmployeeView(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = "add_employee.html/"
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employee')


#update employee view
class UpdateEmployeeView(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = "update_employee.html/"
    form_class = UpdateEmployeeForm
    success_url = reverse_lazy('employee')


#soft delete company
def delete_company(request,pk):
    company = Company.objects.all()
    company_get = Company.objects.get(company_id=pk)
    company_get.soft_del()
    return render(request,'company.html',context={'company':company})


#soft delete employee
def delete_employee(request,pk):
    employee = Employee.objects.all()
    employee_get = Employee.objects.get(employee_id=pk)
    employee_get.soft_del()
    return render(request,'employee.html',context={'employee':employee})


#bin to list soft deleted items
@login_required
def bin(request):
    company = Company.allobj.filter(is_deleted=True)
    employee = Employee.allobj.filter(is_deleted=True)
    return render(request,'bin.html',context={'company':company,'employee':employee})


#restore soft deleted company from bin
@login_required
def restore_company(request,pk):
    company = Company.allobj.filter(is_deleted=True)
    employee = Employee.allobj.filter(is_deleted=True)
    company_get = Company.allobj.get(company_id=pk)
    company_get.restore()
    return render(request,'bin.html',context={'company':company,'employee':employee}) 


#restore soft deleted emloyee from bin
@login_required
def restore_employee(request,pk):
    company = Company.allobj.filter(is_deleted=True)
    employee = Employee.allobj.filter(is_deleted=True)
    employee_get = Employee.allobj.get(employee_id=pk)
    employee_get.restore()
    return render(request,'bin.html',context={'company':company,'employee':employee}) 