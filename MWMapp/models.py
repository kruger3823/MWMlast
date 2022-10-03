from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Jb(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
        profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
        address = models.CharField(max_length=40)
        mobile = models.CharField(max_length=20, null=False)
        status = models.BooleanField(default=False)

        @property
        def get_name(self):
            return self.user.first_name + " " + self.user.last_name

        @property
        def get_instance(self):
            return self

        def __str__(self):
            return self.user.first_name


class Insurance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)




class Patient1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)






















# place1=models.CharField(max_length=200,null=True)
    # address1=models.CharField(max_length=200,null=True)
    # address11=models.CharField(max_length=200,null=True)
    # wages1=models.CharField(max_length=200,null=True) 
    # pan1=models.CharField(max_length=200,null=True)
    # gpay1=models.CharField(max_length=200,null=True) 
    # photo1=models.CharField(max_length=200,null=True)

class fitnessreport(models.Model):
    image= models.ImageField(null=True,blank=True,upload_to="static/")



class insuranceagency(models.Model):
    regno=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    type1=models.CharField(max_length=200,null=True) 
    no=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True) 
    password2=models.CharField(max_length=200,null=True)

class insurance_scheme(models.Model):
    policyno= models.CharField(max_length=200, null=True)
    insurancetype= models.CharField(max_length=200, null=True)
    company= models.CharField(max_length=200, null=True)
    policyDescription= models.CharField(max_length=200, null=True)
    timelength= models.CharField(max_length=200, null=True)
    insuranceamount= models.CharField(max_length=200, null=True)

class insurance_scheme1(models.Model):
        policyno = models.CharField(max_length=200, null=True)
        insurancetype = models.CharField(max_length=200, null=True)
        company = models.CharField(max_length=200, null=True)
        policyDescription = models.CharField(max_length=200, null=True)
        timelength = models.CharField(max_length=200, null=True)
        insuranceamount = models.CharField(max_length=200, null=True)





class jobs(models.Model):
    jbtitle=models.CharField(max_length=200,null=True)
    jbplace=models.CharField(max_length=200,null=True)
    jbdate=models.CharField(max_length=200,null=True)
    jbname=models.CharField(max_length=200,null=True) 
    jbdes=models.CharField(max_length=200,null=True)
    jbno=models.CharField(max_length=200,null=True) 

class applyjobs(models.Model):
    jbtitle=models.CharField(max_length=200,null=True)
    jbplace=models.CharField(max_length=200,null=True)
    jbdate=models.CharField(max_length=200,null=True)
    jbname=models.CharField(max_length=200,null=True)
    jbdes=models.CharField(max_length=200,null=True)
    jbno=models.CharField(max_length=200,null=True)


class complaintjb(models.Model):
    complaintsub=models.CharField(max_length=200,null=True)
    complaintdes=models.CharField(max_length=200,null=True)

class complaintin(models.Model):
    complaintsub=models.CharField(max_length=200,null=True)
    complaintdes=models.CharField(max_length=200,null=True)



class complaintworker(models.Model):
    complaintsub=models.CharField(max_length=200,null=True)
    complaintdes=models.CharField(max_length=200,null=True)
   

# class fitness(models.Model):
#     complaintsub=models.CharField(max_length=200,null=True)
#     complaintdes=models.CharField(max_length=200,null=True)

class Product(models.Model):
    eye = models.ImageField(upload_to='media/')
    adhar = models.ImageField(upload_to='media/')
    fitness = models.ImageField(upload_to='media/')
    yesno = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False)


    