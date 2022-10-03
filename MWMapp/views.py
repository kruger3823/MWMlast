from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from . import models
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

# Create your views here.
from . import forms, models
from .forms import WorkerForm
from .models import Worker

from . import *
from .forms import ProductForm
from .models import Product

from .models import jobs
from .forms import *
from django.core.files.storage import FileSystemStorage


# Create your views here.

def registerUserpage(request):
    userForm= WorkerUserForm()
    workerForm= WorkerForm()
    mydict={'userForm':userForm,'workerForm':workerForm}
    if request.method=='POST':
        userForm= WorkerUserForm(request.POST)
        customerForm= WorkerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            print(user)
            worker=customerForm.save(commit=True)
            worker.user=user
            worker.save()
            print(worker)
            my_worker_group = Group.objects.get_or_create(name='WORKER')
            my_worker_group[0].user_set.add(user)
        return redirect('/workerlogin')
    return render(request,'workersignup.html',context=mydict)




def updateworker(request):
    print("hey",request.user.id)
    user = models.User.objects.get(id=request.user.id)
    userForm=WorkerUserForm(instance=user)
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=WorkerUserForm(request.POST,instance=user)

        if userForm.is_valid():
            print("working")
            user=userForm.save(commit=True)
            user.set_password(user.password)
            user.save()


            return redirect('workerdash/')
    return render(request,'workersignup.html',context=mydict)


def regjobproviderpage(request):
    userForm= JbUserForm()
    workerForm= JbForm()
    mydict={'userForm':userForm,'workerForm':workerForm}
    if request.method=='POST':
        userForm= JbUserForm(request.POST)
        customerForm= JbForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            print(user)
            worker=customerForm.save(commit=True)
            worker.user=user
            worker.save()
            print(worker)
            my_worker_group = Group.objects.get_or_create(name='JB')
            my_worker_group[0].user_set.add(user)
        return HttpResponseRedirect('/workerlogin')
    return render(request,'workersignup.html',context=mydict)

def updatejb(request):
    print("hey",request.user.id)
    user = models.User.objects.get(id=request.user.id)
    userForm=JbUserForm(instance=user)
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=JbUserForm(request.POST,instance=user)

        if userForm.is_valid():
            print("working")
            user=userForm.save(commit=True)
            user.set_password(user.password)
            user.save()


            return redirect('jbdash/')
    return render(request,'workersignup.html',context=mydict)


def reginsurancepage(request):
    userForm= InsuranceUserForm()
    workerForm= InsuranceForm()
    mydict={'userForm':userForm,'workerForm':workerForm}
    if request.method=='POST':
        userForm= InsuranceUserForm(request.POST)
        customerForm= InsuranceForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            print(user)
            worker=customerForm.save(commit=True)
            worker.user=user
            worker.save()
            print(worker)
            my_worker_group = Group.objects.get_or_create(name='INSURANCE')
            my_worker_group[0].user_set.add(user)
        return redirect('workerlogin')
    return render(request,'workersignup.html',context=mydict)

def updatein(request):
    print("hey",request.user.id)
    user = models.User.objects.get(id=request.user.id)
    userForm=InsuranceUserForm(instance=user)
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=InsuranceUserForm(request.POST,instance=user)

        if userForm.is_valid():
            print("working")
            user=userForm.save(commit=True)
            user.set_password(user.password)
            user.save()


            return redirect('insurance_dash/')
    return render(request,'workersignup.html',context=mydict)



def is_police(user):
    return user.groups.filter(name='ADMIN').exists()
def is_worker(user):
    return user.groups.filter(name='WORKER').exists()
def is_jb(user):
    return user.groups.filter(name='JB').exists()
def is_insurance(user):
    return user.groups.filter(name='INSURANCE').exists()

def afterlogin_view(request):
    if is_police(request.user):
        return redirect('police_dash')
    elif is_worker(request.user):
        accountapproval=models.Worker.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('workerdash')
        else:
            return render(request,'ef_wait_for_approval.html')
    elif is_jb(request.user):
        accountapproval=models.Jb.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('jbdash')
        else:
            return render(request,'ef_wait_for_approval.html')
    elif is_insurance(request.user):
        accountapproval=models.Insurance.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('insurance_dash')
        else:
            return render(request,'ef_wait_for_approval.html')


def admin_approve_worker(request):
    #those whose approval are needed
    doctors=models.Worker.objects.all().filter(status=False)
    return render(request,'admin_approve_worker.html',{'doctors':doctors})

def admin_approve_jb(request):
    #those whose approval are needed
    doctors=models.Jb.objects.all().filter(status=False)
    return render(request,'admin_approve_jb.html',{'doctors':doctors})

def admin_approve_insurance(request):
    #those whose approval are needed
    doctors=models.Insurance.objects.all().filter(status=False)
    return render(request,'admin_approve_insurance.html',{'doctors':doctors})




def approveworkers(request,id):
    prod = Worker.objects.get(pk=id)
    prod.status = True
    prod.save()
    return redirect(reverse('approve-worker'))

def approvejb(request,id):
    prod = Jb.objects.get(pk=id)
    prod.status = True
    prod.save()
    return redirect(reverse('approve-jb'))


def approveinsurance(request,id):
    prod = Insurance.objects.get(pk=id)
    prod.status = True
    prod.save()
    return redirect(reverse('approve-insurance'))



def jobapply(request):

    patientForm=PatientForm()
    mydict={'patientForm':patientForm}
    if request.method=='POST':
        print("hi")
        patientForm=PatientForm(request.POST,request.FILES)
        if patientForm.is_valid():
            print("hi")
            patient=patientForm.save(commit=False)
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()

        return render(request,'patientsignup.html',context=mydict)
    return render(request,'patientsignup.html',context=mydict)


def jbapplyview(request):
    patients=models.Patient.objects.all().filter(status=False,assignedDoctorId=request.user.id)
    return render(request,'jobapplyview.html',{'patients':patients})




def applyinsurance(request):

    patientForm=PatientForm1()
    mydict={'patientForm':patientForm}
    if request.method=='POST':
        print("hi")
        patientForm=PatientForm1(request.POST,request.FILES)
        if patientForm.is_valid():
            print("hi")
            patient=patientForm.save(commit=False)
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()

        return render(request,'patientsignup.html',context=mydict)
    return render(request,'patientsignup.html',context=mydict)


def insuranceapplyview(request):
    patients=models.Patient1.objects.all().filter(status=False,assignedDoctorId=request.user.id)
    return render(request,'jobapplyview.html',{'patients':patients})




def workerfitapply(request):
    patients=models.Product.objects.all().filter(status=False)
    return render(request,'fitnessapplyview.html',{'patients':patients})



def approvefitness(request,id):
    prod = Product.objects.get(pk=id)
    prod.status = True
    prod.save()
    return redirect('police_dash')






















































































def registerUser(request):
    page = 'register'
    form = AdminSigupForm()

    if request.method == 'POST':

        form = AdminSigupForm(request.POST)
        if form.is_valid():
            print("hui")
            user = form.save(commit=False)
            user.save()
            return redirect('index')

    context = {'form': form, 'page': page}
    return render(request, 'regworker.html', context)


def jbUser(request):
    page = 'register'
    form = jbSigupForm()

    if request.method == 'POST':

        form = jbSigupForm(request.POST)
        if form.is_valid():
            print("hui")
            user = form.save(commit=False)
            user.save()
            return redirect('index')

    context = {'form': form, 'page': page}
    return render(request, 'regworker.html', context)




# indexpage-home
def index(request):
    return render(request,'index.html')
# about page
def about(request):
    return render(request,'about.html')

 # services page   
def services(request):
    return render(request,'services.html')

  # contact page   
def contact(request):
    return render(request,'contact.html')

 # form page   
def form(request):
    return render(request,'form.html')

def example(request):
    return render(request,'example.html')

# form page   
# def index1_profile(request):
#     return render(request,'index1_profile.html')

 



# dash board  
def workerdash(request):
    return render(request,'workerdash.html')

def jbdash(request):
    return render(request,'jbdash.html')

def index2(request):
    return render(request,'index2.html')


# welcome page example
def home(request):

    id=request.session['id']
    username=request.session['username']
    # email=request.session['name']
    return render(request,'home.html',{'id':id,'username':username})

def home1(request):

    id=request.session['id']
    name=request.session['name']
    # email=request.session['name']
    return render(request,'home1.html',{'id':id,'name':name})

# dashborad
# def index1(request):

#     id=request.session['id']
#     username=request.session['username']
#     # email=request.session['name']
#     return render(request,'index1.html',{'id':id,'username':username})  
# dashboard


# ------worker------

 #  worker register page


# -----additional info-----worker dashboard


  # -----additional info----- worker dashboard   

# def view(request):
#     cr=additionalinfo1.objects.all()
#     return render(request,'worker_profile.html',{'cr':cr})







def jb_addjob(request):
    if request.method=="POST":
        jbtitle=request.POST.get('jbtitle')
        jbplace=request.POST.get('jbplace')
        jbdate=request.POST.get('jbdate')
        jbname=request.POST.get('jbname')
        jbdes=request.POST.get('jbdes')
        jbno=request.POST.get('jbno')
    
        jobs(jbtitle=jbtitle,jbplace=jbplace,jbdate=jbdate,jbdes=jbdes,jbname=jbname,jbno=jbno).save()
    return render(request,'jb_addjob.html')


def jb_apply(request):
    if request.method == "POST":
        jbtitle = request.POST.get('jbtitle')
        jbplace = request.POST.get('jbplace')
        jbdate = request.POST.get('jbdate')
        jbname = request.POST.get('jbname')
        jbdes = request.POST.get('jbdes')
        jbno = request.POST.get('jbno')

        applyjobs(jbtitle=jbtitle, jbplace=jbplace, jbdate=jbdate, jbdes=jbdes, jbname=jbname, jbno=jbno).save()
    return render(request, 'jb_applyjob.html')

def jb_apply1(request):
    if request.method == "POST":
        policyno = request.POST.get('policyno')
        insurancetype= request.POST.get('insurancetype')
        company = request.POST.get('company')
        timelength = request.POST.get('timelength')
        policyDescription = request.POST.get('policyDescription')
        insuranceamount = request.POST.get('insuranceamount')

        insurance_scheme(policyno=policyno,insurancetype=insurancetype,company=company,timelength=timelength,policyDescription=policyDescription,insuranceamount=insuranceamount).save()
    return render(request,'jb_applyjob1.html')




def add_scheme(request):
    if request.method == "POST":
        policyno = request.POST.get('policyno')
        insurancetype= request.POST.get('insurancetype')
        company = request.POST.get('company')
        timelength = request.POST.get('timelength')
        policyDescription = request.POST.get('policyDescription')
        insuranceamount = request.POST.get('insuranceamount')

        insurance_scheme(policyno=policyno,insurancetype=insurancetype,company=company,timelength=timelength,policyDescription=policyDescription,insuranceamount=insuranceamount).save()
    return render(request,'add_scheme.html')



def jbcomplaint(request):
    if request.method=="POST":
        complaintsub=request.POST.get('complaintsub')
        complaintdes=request.POST.get('complaintdes')
        
        complaintjb(complaintsub=complaintsub,complaintdes=complaintdes).save()
    return render(request,'jbcomplaint.html')


def worker_fitness(request):
    if request.method == 'POST':
        form = fitnessreport(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = fitnessreport()
    return render(request, 'add_scheme.html', {'form': form})







    #  workerlogin page
def login(request):
    return render(request,'login.html')

#  worker login function
def log(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        cr=worker.objects.filter(email=email,password=password)
        if cr:
            user=worker.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            username=user.username
            email=user.email
            print('email',email)
     

            request.session['id']=id
            
            request.session['email']=email
            request.session['username']=username

            

            return redirect('workerdash')
        else:
            return render(request,'login.html')
    else:
        return render(request,'regworker.html')

# -------worker------

# -------job provider------

 #  job provider register page
def regjobprovider(request):
    if request.method=="POST":
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        no=request.POST.get('no')
        photoid=request.POST.get('photoid')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        jobprovider(user_name=user_name,email=email,dob=dob,gender=gender,photoid=photoid,no=no,password=password,password2=password2).save()
        return redirect('jblogin')
    else:
        return render(request,'regjobprovider.html') 
    # info=None
    # try:
    #     user=worker.objects.get(id=request.session['id'])
    #     info=user.jobprovider
    # except:
    #     pass    
    #     return redirect('jblogin')
    # else:
    # return render(request,'regjobprovider.html',{"info":info})  

#  job provider login page
def jblogin(request):
    return render(request,'jblogin.html')
    
#  job provider login function    
def log1(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
       
      
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        jb=jobprovider.objects.filter(email=email,password=password)
        if jb:
            user=jobprovider.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            user_name=user.user_name
            email=user.email
            print('email',email)
     
            request.session['id']=id
            
            request.session['email']=email
            request.session['user_name']=user_name

            return redirect('jbdash')
        else:
            return render(request,'jblogin.html')
    else:
        return render(request,'regjobprovider.html')

# -----job provider----


# -----insurance agency----

# insurance agency register page
def reginsurance(request):
    if request.method=="POST":
        regno=request.POST.get('regno')
        name=request.POST.get('name')
        email=request.POST.get('email')
        type1=request.POST.get('type1')
        no=request.POST.get('no')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        insuranceagency(regno=regno,name=name,email=email,type1=type1,no=no,password=password,password2=password2).save()
        return redirect('insurancelogin')
    else:
        return render(request,'reginsurance.html')  
         
 #  insurance agency login page
def insurancelogin(request):
    return render(request,'insurancelogin.html')

#  insurance agency  login function
def log2(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        cr=insuranceagency.objects.filter(email=email,password=password)
        if cr:
            user=insuranceagency.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            name=user.name
            email=user.email
            print('email',email)
           
           
            

            request.session['id']=id
            
            request.session['email']=email
            request.session['name']=name

            

            return redirect('insurance_dash')
        else:
            return render(request,'insurancelogin.html')
    else:
        return render(request,'reginsurance.html')


def insurance_dash(request):
    return render(request,'insurance_dash.html')

# -----insurance agency----


# -----police----

# # insurance agency register page
# def reginsurance(request):
#     if request.method=="POST":
#         regno=request.POST.get('regno')
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         type1=request.POST.get('type1')
#         no=request.POST.get('no')
#         password=request.POST.get('password')
#         password2=request.POST.get('password2')

#         insuranceagency(regno=regno,name=name,email=email,type1=type1,no=no,password=password,password2=password2).save()
#         return redirect('insurancelogin')
#     else:
#         return render(request,'reginsurance.html')  
         
 # police login page
def policelogin(request):
    return render(request,'policelogin.html')

#  police login function
def log3(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'police_dash.html', {'page': page})
    # else:
    #     return render(request,'index.html')

def police_dash(request):
    return render(request,'police_dash.html')


# ----police----



def worker_viewprof(request):
    cr=additionalinfo1.objects.all()
    return render(request,'worker_viewprof.html',{'cr':cr})



def jb_viewprof(request):
    jb=jobprovider.objects.all()
    # print('user_name',user_name)

    return render(request,'jb_viewprof.html',{'jb':jb})

# def worker_viewprof(request):
#     return render(request,'worker_viewprof.html')


def worker_changepass(request):
        if request.method == "POST":
            password = request.POST.get('password')


            print('password', password)
            # print('password')
            # print(password)

            cr = worker.objects.filter(password=password)
            if cr:
                user = worker.objects.get(password=password)
                print(password)
                id = user.id
                print('id', id)
                password = user.password



                request.session['id'] = id


                request.session['password'] = password
                print(password)

                return redirect('workerdash')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'regworker.html')


def worker_viewjob(request):
    job_view = jobs.objects.all() #.filter(status=True)
    return render(request, 'worker_viewjob.html', {'job_view': job_view})


def worker_complaint(request):
    if request.method=="POST":
        complaintsub=request.POST.get('complaintsub')
        complaintdes=request.POST.get('complaintdes')
        
        complaintworker(complaintsub=complaintsub,complaintdes=complaintdes).save()
    return render(request,'worker_complaint.html')

# def jb_viewprof(request):
#     return render(request,'jb_viewprof.html')


def jb_changepass(request):
    return render(request,'jb_changepass.html')

def worker_viewappliedjob(request):
    job_view = Patient.objects.all().filter()
    return render(request, 'worker_viewappliedjob.html', {'job_view': job_view})


def worker_viewappliedpolicy(request):
    job_view = Patient1.objects.all().filter()  # .filter(status=True)
    return render(request, 'worker_viewappliedpolicy.html', {'job_view': job_view})


def worker_viewpolicy(request):
    insurance_view = insurance_scheme.objects.all()  # .filter(status=True)
    return render(request,'worker_viewpolicy.html',{'insurance_view': insurance_view})

#def worker_viewappliedpolicy(request):
 #   job_view = applyjobs.objects.all()  # .filter(status=True)
  #  return render(request,'worker_viewappliedpolicy.html',{'job_view': job_view})


def jb_viewaddedjob(request):
    job_view = jobs.objects.all()  # .filter(status=True)
    return render(request,'jb_viewaddedjob.html',{'job_view': job_view})

def jb_viewaddedjob1(request):
    job_view = insurance_scheme.objects.all()

    return render(request,'jb_viewaddedjob1.html',{'job_view': job_view})

def jb_viewaddedjob2(request):
    job_view = insurance_scheme.objects.all()  # .filter(status=True)
    return render(request,'jb_viewaddedjob2.html',{'job_view': job_view})

def worker_viewcomp(request):
    job_view = complaintworker.objects.all()  # .filter(status=True)
    return render(request,'complaintsub.html',{'job_view': job_view})

def worker_viewcompjb(request):
    job_view = complaintjb.objects.all()  # .filter(status=True)
    return render(request,'complaintsubJB.html',{'job_view': job_view})

def worker_viewcompin(request):
    job_view = complaintin.objects.all()  # .filter(status=True)
    return render(request,'complaintsubin.html',{'job_view': job_view})


def workerview(request):
    job_view = Worker.objects.all()  # .filter(status=True)
    return render(request,'adminworkerview.html',{'job_view': job_view})

def jbview(request):
    job_view = Jb.objects.all()  # .filter(status=True)
    return render(request,'adminjbview.html',{'job_view': job_view})

def inview(request):
    job_view = Insurance.objects.all()  # .filter(status=True)
    return render(request,'adminjbview.html',{'job_view': job_view})





def logout(request):
    return render(request,'index.html')



def pdf_report_create(request):
    products = jobs.objects.all()

    template_path = 'MWMapp/jb_viewaddedjobs.html'

    context = {'products': products}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        print("hii")
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workerdash')
    else:
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, 'worker_fitness.html', context)




def apply(request):

    patientForm=forms.PatientForm()
    mydict={'patientForm':patientForm}
    if request.method=='POST':

        patientForm=forms.PatientForm(request.POST,request.FILES)
        if patientForm.is_valid():
            patient=patientForm.save(commit=False)
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()

        return render(request,'patientsignup.html',context=mydict)
    return render(request,'patientsignup.html',context=mydict)

def appliedjob_view(request):
    #for three cards
    patientcount=models.worker.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()

    mydict={
    'patientcount':patientcount,
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)




