from django.contrib.auth.views import LoginView
from django.urls import path
from.import views
from django.conf.urls.static import static,settings




urlpatterns=[
    path('',views.index,name="index"),
    path('jb/',views.registerUser,name="regworker_view"),
path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),

path('approve-worker', views.admin_approve_worker, name='approve-worker'),
    path('approve/<int:id>',views.approveworkers,name="approve"),

path('approve-jb', views.admin_approve_jb, name='approve-jb'),
    path('approve1/<int:id>',views.approvejb,name="approve1"),

path('approve-insurance', views.admin_approve_insurance, name='approve-insurance'),
    path('approve2/<int:id>',views.approveinsurance,name="approve2"),


path('workerfitapply',views.workerfitapply,name='workerfitapply'),
    path('approvefitness/<int:id>',views.approvefitness,name="approvefitness"),





# ----worker-reg---
path('regworker',views.registerUserpage,name="regworker"),
path('updateworker',views.updateworker,name='updateworker'),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
    path('workerlogin', LoginView.as_view(template_name='workerlogin.html'), name="workerlogin"),
# ----worker-reg---

# ----jobprovider-reg---
path('updatejb',views.updatejb,name='updatejb'),
    path('regjb',views.regjobproviderpage,name="regjb"),
    path('jblogin', LoginView.as_view(template_name='workerlogin.html'), name="jblogin"),
    path('log1/',views.log1,name="log1"),
    path('job_view',views.jobs,name="job_view"),
# ----jobprovider-reg---

# ----insurance-reg---
path('updatein',views.updatein,name='updatein'),
    path('reginsurance',views.reginsurancepage,name="reginsurance"),
    path('insurancelogin',views.insurancelogin,name="insurancelogin"),
    path('log2/',views.log2,name="log2"),
# ----insurance-reg---

# ----police-reg---

    path('policelogin',views.policelogin,name="policelogin"),
    path('log3/',views.log3,name="log3"),
# ----police-reg---



     path('home/',views.home,name="home"),
     path('home1/',views.home1,name="home1"),

# dashbord
     path('workerdash/',views.workerdash,name="workerdash"),
     path('index2/',views.index2,name="index2"),
# dashbord
     path('form/',views.form,name="form"),
     #path('worker_profile/',views.worker_profile,name="worker_profile"),
     path('jbdash/',views.jbdash,name="jbdash"),



     path('apply_policy',views.applyinsurance,name="apply_policy"),
path('appliedpolicy',views.insuranceapplyview,name="appliedpolicy"),
     path('jobapply',views.jobapply,name="jobapply"),
    path('viewapply',views.jbapplyview,name="viewapply"),

     path('jb_addjob',views.jb_addjob,name="jb_addjob"),
     path('example',views.example,name="example"),
     path('jbcomplaint',views.jbcomplaint,name="jbcomplaint"),
     #path('worker_fitness/',views.worker_fitness,name="worker_fitness"),
    #  path('view/',views.view,name="view"),
     path('worker-profile',views.worker_viewprof,name="worker-profile"),
     path('worker_changepass',views.worker_changepass,name="worker_changepass"),
     path('worker_viewjob',views.worker_viewjob,name="worker_viewjob"),
    path('worker_fitness', views.addProduct, name="worker_fitness"),
    path('worker_complaint',views.worker_complaint,name="worker_complaint"),
     path('jb_viewprof',views.jb_viewprof,name="jb_viewprof"),
     path('jb_changepass',views.jb_changepass,name="jb_changepass"),
     path('insurance_dash',views.insurance_dash,name="insurance_dash"),


     path('police_dash',views.police_dash,name="police_dash"),

     path('worker_viewappliedjob',views.worker_viewappliedjob,name="worker_viewappliedjob"),
     path('worker_viewpolicy',views. worker_viewpolicy,name="worker_viewpolicy"),
     path('worker_viewappliedpolicy',views.worker_viewappliedpolicy,name="worker_viewappliedpolicy"),
     path('jb_viewaddedjob',views.jb_viewaddedjob,name="jb_viewaddedjob"),
    path('view_scheme',views.jb_viewaddedjob1,name="view_scheme"),
     path('add_scheme',views.add_scheme,name="add_scheme"),
     path('logout', views.logout, name="logout"),
path('worker_viewcomp',views.worker_viewcomp,name="worker_viewcomp"),
path('worker_viewcompjb',views.worker_viewcompjb,name="worker_viewcompjb"),
path('worker_viewcompin',views.worker_viewcompin,name="worker_viewcompin"),
path('workerview',views.workerview,name="workerview"),
path('jbview',views.jbview,name="jbview"),
path('inview',views.inview,name="inview"),


]
