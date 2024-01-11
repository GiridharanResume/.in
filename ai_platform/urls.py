
from django.urls import path, include
from django.http import HttpResponse
from ai_platform import views



urlpatterns = [
    path('', views.indexpage,name='index'),
    path('home/', views.home,name='home'),
    path('login/', views.loginpage,name='login'),
    path('logout/', views.login),
    path('KTcoursepage/',views.KTcoursepage,name='KTcoursepage'),
    path('ADAScourse/',views.ADAScourse,name='ADAScourse'),
    path('PYTHONcourse/',views.PYTHONcourse,name='PYTHONcourse'),
    path('RPIcourse/',views.RPIcourse,name='RPIcourse'),
    path('NANOcourse/',views.NANOcourse,name='NANOcourse'),
    path('AIcourse/',views.AIcourse,name='AIcourse'),
    path('DScourse/',views.DScourse,name='DScourse'),
    path('admin_user/',views.admin_user,name='admin_user'),
    path('subadmin/',views.subadminpage,name='subadmin'),
    path('subadminmain/',views.subadminmain,name='subadminmain'),
    path('subadminhome/',views.subadmin_verify,name='subadminhome'),
    path('KTcontent/',views.KTcontent,name='KTcontent'),
    path('ADAScontent/',views.ADAScontent,name='ADAScontent'),
    path('PYTHONcontent/',views.PYTHONcontent,name='PYTHONcontent'),
    path('RPIcontent/',views.RPIcontent,name='RPIcontent'),
    path('NANOcontent/',views.NANOcontent,name='NANOcontent'),
    path('AIcontent/',views.AIcontent,name='AIcontent'),
    path('DScontent/',views.DScontent,name='DScontent'),
    path('Editcontent/',views.Editcontentpage,name='Editcontent'),
    path('signup/',views.signuppage,name='signup'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('userhome/', views.userhomepage,name='userhome'),
    path('profile/', views.profilepage,name='profile'),
    path('mycourse/', views.mycoursepage,name='mycourse'),
    path('KTEnroll/', views.KTEnrollpage,name='KTEnroll'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('KTHomepage/', views.KTHomepage,name='KTHomepage'),
    path('Add-topic/', views.Addtopic,name='Add-topic'),
    path('Mentor/', views.mentorpage,name='Mentor'),
    path('Edit-Mentor/', views.Editmentor,name='Edit-Mentor'),
    path('Forgetpassword/', views.Forgetpassword,name='Forgetpassword'),
    path('Editadmin/', views.Editadmin,name='Editadmin'),
    path('Editsubadmin/', views.Editsubadmin,name='Editsubadmin'),
    
    
    
]
