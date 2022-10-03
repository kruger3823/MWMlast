from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


from django import forms
from . import models
from django.contrib.auth.models import User

class WorkerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model= models.Worker
        fields=['address','mobile','profile_pic']


class JbUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class JbForm(forms.ModelForm):
    class Meta:
        model= models.Jb
        fields=['address','mobile','profile_pic']




class InsuranceUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class InsuranceForm(forms.ModelForm):
    class Meta:
        model= models.Insurance
        fields=['address','mobile','profile_pic']



class PoliceForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend docto
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Jb.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']



class PatientForm1(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend docto
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Insurance.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient1
        fields=['address','mobile','status','symptoms','profile_pic']



















class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(AdminSigupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})

class jbSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(jbSigupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})





                #    'place':forms.TextInput(attrs={'class' :'form-control'}),
                #    'address':forms.TextInput(attrs={'class' :'form-control'}),
                #    'address1':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'wages':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'pan':forms.TextInput(attrs={'class' :'form-control'}),
                #    'gpay':forms.TextInput(attrs={'class' :'forms-control'}),

class addjob(forms.ModelForm):
    class Meta:
        model=jobs
        fields=('jbtitle','jbplace','jbdate','jbname','jbdes','jbno')
        widigets={


                   'jbtitle':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbplace':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbdate':forms.TextInput(attrs={'class' :'forms-control'}),
                   'jbname':forms.TextInput(attrs={'class' :'forms-control'}),
                   'jbdes':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbno':forms.TextInput(attrs={'class' :'forms-control'}),
                  
        }


class applyjob(forms.ModelForm):
    class Meta:
        model = jobs
        fields = ('jbtitle', 'jbplace', 'jbdate', 'jbname', 'jbdes', 'jbno')
        widigets = {

            'jbtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'jbplace': forms.TextInput(attrs={'class': 'form-control'}),
            'jbdate': forms.TextInput(attrs={'class': 'forms-control'}),
            'jbname': forms.TextInput(attrs={'class': 'forms-control'}),
            'jbdes': forms.TextInput(attrs={'class': 'form-control'}),
            'jbno': forms.TextInput(attrs={'class': 'forms-control'}),

        }


class addcomplaint(forms.ModelForm):
    class Meta:
        model=complaintjb
        fields=('complaintsub','complaintdes')
        widigets={


                   'complaintsub':forms.TextInput(attrs={'class' :'form-control'}),
                   'complaintdes':forms.TextInput(attrs={'class' :'form-control'}),
                  
                  
        }   


class addcomplaint1(forms.ModelForm):
    class Meta:
        model=complaintworker
        fields=('complaintsub','complaintdes')
        widigets={


                   'complaintsub':forms.TextInput(attrs={'class' :'form-control'}),
                   'complaintdes':forms.TextInput(attrs={'class' :'form-control'}),
                  
                  
        }   













class registerjb(forms.ModelForm):
    class Meta:
        model=insuranceagency
        fields=('regno','name','email','type1','no','password','password2')
        widigets={

                  
                   'regno':forms.TextInput(attrs={'class' :'form-control'}),
                   'name':forms.TextInput(attrs={'class' :'form-control'}),
                   'email':forms.TextInput(attrs={'class' :'forms-control'}),
                   'type1':forms.TextInput(attrs={'class' :'forms-control'}),
                   'no':forms.TextInput(attrs={'class' :'form-control'}),
                   'password':forms.TextInput(attrs={'class' :'forms-control'}),
                   'password2':forms.TextInput(attrs={'class' :'forms-control'}),
        }   



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['eye', 'adhar', 'fitness', 'yesno']
        widgets = {
            'eye': forms.FileInput(attrs={'class': 'form-control'}),
            'adhar': forms.FileInput(attrs={'class': 'form-control'}),
            'fitness': forms.FileInput(attrs={'class': 'form-control'}),
            'yesno': forms.TextInput(attrs={'class': 'form-control'}),

        }







