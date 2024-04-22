from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="home"),
    path('companies/', views.company, name='company'),
    path('employee/', views.employee, name='employee'),
    path('add-company/', views.CreateCompanyView.as_view(), name='add-company'),
    path('update-company/<pk>', views.UpdateCompanyView.as_view(), name='update-company'),
    path('add-employee/', views.CreateEmployeeView.as_view(), name='add-employee'),
    path('update-employee/<pk>', views.UpdateEmployeeView.as_view(), name='update-employee'),
    path('delete-company/<pk>',views.delete_company,name='delete-company'),
    path('delete-employee/<pk>',views.delete_employee,name='delete-employee'),
    path('bin/',views.bin,name='bin'),
    path('restore-company/<pk>',views.restore_company,name='restore-company'),
    path('restore-employee/<pk>',views.restore_employee,name='restore-employee'),

]

