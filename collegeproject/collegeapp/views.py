from django.shortcuts import render,redirect
from django.http import HttpResponse
from collegeapp.models import Department,User,Teacher,Student
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def adddep(request):
    if  request.method=="GET":
        return render(request,'add_dep.html')
    elif request.method == "POST":
        dep = request.POST['department']
        x=Department.objects.create(Dep_Name=dep)
        x.save()
        return HttpResponse("<script>alert('added successfully');</script>")
def teacher_reg(request):
    if request.method=="GET":
        data=Department.objects.all()
        return render(request,'treg.html',{'data1':data})
    elif request.method =="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        p=request.POST['pass']
        e=request.POST['email']
        a=request.POST['add']
        ph=request.POST['phone']
        ag=request.POST['age']
        q=request.POST['qual']
        d=request.POST['dep']
        x=User.objects.create_user(first_name=f,last_name=l,username=u,password=p,email=e,usertype='teacher')
        x.save()
        y =Teacher.objects.create(user_id=x,dep_id_id=d,Address=a,age=ag,Qualification=q,Phone=ph)
        y.save()
        return HttpResponse("<script>alert('successfully Registered');</script>")
def student(request):
    if  request.method=="GET":
        data=Department.objects.all()
        return render(request,'student.html',{'data1':data})
    elif request.method == "POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        p=request.POST['pass']
        e=request.POST['email']
        a=request.POST['add']
        ph=request.POST['phone']
        d=request.POST['dep']
        x=User.objects.create_user(first_name=f,last_name=l,username=u,password=p,email=e,usertype='student',is_active = False)
        x.save()
        y =Student.objects.create(user_id=x,dep_id_id=d,Address=a,Phone=ph)
        y.save()
        return HttpResponse("<script>alert(' Student registration successfull');</script>")
def studentview(request):
    data=Student.objects.all()
    return render(request,'sview.html',{'data1':data})
def adminhome(request):
    return render(request,'adminhome.html')
def home(request):
    return render(request,'home.html')
def approvest(request,uid):
    stud=Student.objects.get(id=uid)
    stud.user_id.is_active=True
    stud.user_id.save()
    return redirect(studentview)
def logins(request):
    if request.method == "GET":
        return render(request,'logins.html')
    elif request.method == "POST":
        un=request.POST['uname']
        ps=request.POST['pass']
        print(un,ps)
        user=authenticate(request,username=un,password=ps)
        if user is not None and user.usertype=="teacher":
            login(request,user)
            request.session['tech_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=="student"and user.is_active==1:
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studenthome)
        elif user is not None and user.is_superuser==1:
            return redirect(adminhome)
        else:
            return HttpResponse("not valid")
    return HttpResponse("not okk")

def teacherhome(request):
    return render(request,'teacherhome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def lgout(request):
    logout(request)
    return redirect(logins)
def teacherview(request):
    data=Teacher.objects.all()
    return render(request,'tview.html',{'data1':data})
def updateprofile(request):
    stud=request.session.get('stud_id')
    st=Student.objects.get(user_id_id=stud)
    us=User.objects.get(id=stud)
    return render(request,'updateprofile.html',{'view':st,'data':us})

def update_student(request,uid):
    if request.method == "POST":
        stud=Student.objects.get(id=uid)
        sid=stud.user_id_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()
        stud.Address=request.POST['address']
        stud.Phone=request.POST['phone']
        stud.save()
        return HttpResponse("success")
def updateprofile_t(request):
    teach=request.session.get('tech_id')
    te=Teacher.objects.get(user_id_id=teach)
    uss=User.objects.get(id=teach)
    return render(request,'updateprofile_t.html',{'view':te,'data':uss})
def update_teacher(request,uid):
    if request.method == "POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.user_id_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()
        teach.Address=request.POST['address']
        teach.Phone=request.POST['phone']
        teach.Qualification=request.POST['qualification']
        teach.age=request.POST['age']
        teach.save()
        return HttpResponse("success")
def tstudentview(request):
    data=User.objects.filter(is_active=True,usertype='student')
    stud=Student.objects.all()
    print(stud)
    return render(request,'stview.html',{'data':stud})
    



    

    

