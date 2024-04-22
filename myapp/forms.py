from django.forms import ModelForm
from .models import Company, Employee
from django import forms
from datetime import date
from django.db import IntegrityError


class CreateCompanyForm(ModelForm):
    class Meta:
            model = Company
            fields = ('company_id','name')
            widgets = {
                'company_id': forms.TextInput(attrs={
                    'class':'form-control rounded-3',
                    'id':'floatingInput'
                }),
                'name': forms.TextInput(attrs={
                    'class':'form-control rounded-3',
                    'id':'floatingInput'
                }),
            }

class UpdateCompanyForm(ModelForm):
    class Meta:
            model = Company
            fields = ('company_id','name')
            widgets = {
                'company_id': forms.TextInput(attrs={
                    'class':'form-control rounded-3 bg-light',
                    'id':'floatingInput',
                }),
                'name': forms.TextInput(attrs={
                    'class':'form-control rounded-3',
                    'id':'floatingInput'
                }),
            }


class DateInput(forms.DateInput):
    input_type = 'date'



class CreateEmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_id'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}

    def clean_dob(self):
        birthday = self.cleaned_data['dob']
        age = (date.today() - birthday).days / 365
        if age < 18:
            raise forms.ValidationError('Employee must be at least 18 years old.')
        return birthday
    
    class Meta:
        model = Employee
        fields = ('employee_id','first_name','last_name','company_id','dob','email','profile_pic')
        widgets = {
            'employee_id': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'dob': forms.DateInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'type': 'date'
            }),
            
            'email': forms.EmailInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            
        }
    

class UpdateEmployeeForm(ModelForm):
    def clean_dob(self):
        birthday = self.cleaned_data['dob']
        age = (date.today() - birthday).days / 365
        if age < 18:
            raise forms.ValidationError('Employee must be at least 18 years old.')      
        return birthday
    
    class Meta:
        model = Employee
        fields = ('employee_id','first_name','last_name','company_id','dob','email','profile_pic')
        widgets = {
            'employee_id': forms.TextInput(attrs={
                'class':'form-control rounded-3 bg-light',
                'id':'floatingInput',
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),

            'dob': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput',
                'type': 'date'
            }),
            
            'email': forms.EmailInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class':'form-control rounded-3',
                'id':'floatingInput'
            }),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['company_id'].widget.attrs = {'class': 'form-control rounded-3','required': 'required'}