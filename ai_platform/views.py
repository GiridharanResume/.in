from django.shortcuts import render,HttpResponse,redirect
from .models import Staff_admin as Admin 
from .models import Student_subadmin as subadmin
from .models import course_name
from .models import signup 
from .models import mentor
from .models import KTcourse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def indexpage(request):
     return render(request , 'index.html', )

                  
def home(request):
     if request.method=='POST':
            name=request.POST.get('name')
            description=request.POST.get('description')
            my_course= course_name()
            my_course.name = name
            my_course.description = description
            my_course.save()
            return redirect("home")
          
     course = course_name.objects.all()
   
     return render(request , 'home.html',{'course':course} )

def loginpage(request):
     
     if request.method=='POST':
          name=request.POST.get('name')
          password=request.POST.get('password')
          
          my_user = list(signup.objects.filter(name=name).values())[0]
          
          if password == my_user["password"]:
             request.session['name'] = name
             return render(request , 'user-home.html',{'name':request.session['name']} ) 
     else:
               return render(request , 'login.html' )
          
     


def KTcoursepage(request):
    return render(request , 'Kt-students.html', )

def ADAScourse(request):
    return render(request , 'Adas-students.html', )

def PYTHONcourse(request):
    return render(request , 'Python-students.html', )

def RPIcourse(request):
    return render(request , 'Rpi-students.html', )

def NANOcourse(request):
    return render(request , 'Nano-students.html', )

def AIcourse(request):
    return render(request , 'Ai-students.html', )

def DScourse(request):
    return render(request , 'Ds-students.html', )

def admin_user(request):
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          my_admin= Admin()
          my_admin.name = name
          my_admin.email = email
          my_admin.password = password
          my_admin.save()
          
          return redirect("admin_user")
    admin = Admin.objects.all()
         

    return render(request , 'Admin-user.html',{'admin':admin} )
    



def subadminpage(request):
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          my_sub_admin= subadmin()
          my_sub_admin.name = name
          my_sub_admin.email = email
          my_sub_admin.password = password
          my_sub_admin.save()
          return redirect("subadmin")
     sub_admin = subadmin.objects.all()
         

     return render(request , 'subadmin.html',{'sub_admin':sub_admin} )

def subadminmain(request):
     course = course_name.objects.all()
     return render(request , 'subadmin-Home.html',{'course':course})


def subadmin_verify(request):
     if request.method == "POST":
          print(request.POST.get("user_type") )
          if request.POST.get("user_type") == "subadmin":
               data = subadmin.objects.get(name=request.POST.get("name"))

               if request.POST.get("password") == data.password:
                course = course_name.objects.all()
                return render(request,"subadmin-Home.html",{'course':course})
               else:
                   
                    return redirect('login')
            
          elif request.POST.get("user_type") == "admin":
              
               try:
                    name = request.POST['name']
                    password = request.POST['password']
                   
                    datas = list(Admin.objects.filter(name=name).values())[0]
                    print(datas)
                    if len(datas) >0:
                         if password == datas['password']:
                              return redirect('home')
                         else:
                              
                              return redirect('login')
                
               except:
                    
                    return redirect('login')
               
          elif request.POST.get("user_type") == "user":
              
               try:
                    name = request.POST['name']
                    password = request.POST['password']
                   
                    datas = list(signup.objects.filter(name=name).values())[0]
                    print(datas)
                    if len(datas) >0:
                         if password == datas["password"]:
                            request.session['name'] = name
                            course = course_name.objects.all()
                            return render(request , 'user-home.html',{'name':request.session['name'],'course':course} ) 
                         else:
                              
                              return redirect('login')
                
               except:
                    
                    return redirect('login')   
          
                    


def KTcontent(request):
    return render(request , 'Kt-content.html', )                

def ADAScontent(request):
    return render(request , 'Adas-content.html', ) 

def PYTHONcontent(request):
    return render(request , 'Python-content.html', )

def RPIcontent(request):
    return render(request , 'Rpi-content.html', )  

def NANOcontent(request):
    return render(request , 'Nano-content.html', )

def AIcontent(request):
    return render(request , 'Ai-content.html', )    

def DScontent(request):
    return render(request , 'Ds-content.html', )  

def Editcontentpage(request):
    course = course_name.objects.all()
    return render(request , 'Edit-content.html',{'course':course} )  

def signuppage(request):
     return render(request , 'user-signup.html' )

def signup_user(request):
      if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password1=request.POST.get('password1')
          password2=request.POST.get('password2')
          my_signup= signup()
          my_signup.name = name
          my_signup.email = email
          my_signup.password = password1
          my_signup.password = password2
          

          if request.POST.get('password1') == request.POST.get('password2'):
             my_signup.save()
             return redirect('login')
          else:
             print("Password mismatch")
             return redirect('signup')
          
     
     


def userhomepage(request):
    course = course_name.objects.all()
    return render(request , 'user-home.html',{'course':course} ) 


def profilepage(request):
  
        user_id = signup.objects.get(name=request.session["name"])
        print("user",user_id)
        return render(request , 'profile.html',{"data":user_id})

def edit_profile(request):
     if request.method=='POST':
          my_signup=signup.objects.get(name=request.session["name"])
          my_signup.CollegeName=request.POST.get("CollegeName")
          my_signup.Degree=request.POST.get("Degree")
          my_signup.DOB=request.POST.get("DOB")
          my_signup.Phoneno=request.POST.get("Phoneno")
          my_signup.State=request.POST.get("State")

          
          
          my_signup.save()

          return redirect("profile")

def mycoursepage(request):
     return render(request , 'user_course.html')

def KTEnrollpage(request):
     course = course_name.objects.all()
     return render(request , 'KT-Enroll.html',{'course':course})               


def KTHomepage(request):
     course = course_name.objects.all()
     return render(request , 'KT-HOME.html',{'course':course})

def Addtopic(request):
     course = course_name.objects.all()
     return render(request , 'Add-Topic.html',{'course':course})

def mentorpage(request):
     Mentor = mentor.objects.all()
     return render(request , 'Trainer.html',{'Mentor':Mentor})
def Editmentor(request):
     if request.method=='POST':
          image=request.POST.get('image')
          name=request.POST.get('name')
          position=request.POST.get('position')
          my_mentor= mentor()
          my_mentor.name = name
          my_mentor.position = position

          if len(request.FILES)!=0:
               my_mentor.image = image

          my_mentor.save()
          return redirect("Edit-Mentor")
     Mentor = mentor.objects.all()
     course = course_name.objects.all()
     return render(request , 'Edit-Mentor.html',{'course':course, 'Mentor':Mentor})

def Forgetpassword(request):
     return render(request , 'Forgetpassword.html')


def Editadmin(request):
     email = signup.objects.get(name=request.session["name"])
     return render(request , 'Edit-Admin.html' ,{'data':email})


def Editsubadmin(request):
     return render(request , 'Edit-Subadmin.html' )

