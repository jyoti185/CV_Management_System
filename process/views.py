from django.shortcuts import render,redirect
from process.form import Registrationform, ProfileForm
from django.contrib.messages import success
from process.models import RegistrationModel,IndustryMOdel,ProfileMOdel


# Create your views here.
def showindex(request):
    return render(request,'index.html')


def Registration_page(request):
    rf=Registrationform(request.POST)
    if request.method=="POST":
        if rf.is_valid():
            rf.save()
            return redirect('otp_validate')

        else:
            return render(request, "registration.html", {"form": rf})

    else:
      return render(request,"registration.html",{"form":rf})


def otp_validate(request):
    return render(request,'otp_validate.html')


def validate(request):

    try:
       result= RegistrationModel.objects.get(contact_no=request.POST.get("c1"),otp=request.POST.get("c2"))
       if result.status=="Pending":
           result.status="Approved"
           result.save()
           success(request,"Thanks for Your Registration")
           return redirect('confirmation')
       elif result.status=="Approved":
           success(request, "Your Registration is already Approved ")
           return redirect('confirmation')


    except RegistrationModel.DoesNotExist:
        message="please enter the valid input"
        return render(request,"otp_validate.html",{"message":message})



def    confirmation(request):

    return render(request,"confirmation.html")


def welcome_page(request):
    return render(request,"welcome_page.html")


def validate_login(request):
    try:
        result=RegistrationModel.objects.get(Email_id=request.POST.get('u1'),password=request.POST.get('u2'))
        if result.status=="Pending":
            return render(request, 'otp_validate.html', {"error": "Sorry Your Registration is Pending"})
        if result.status=="closed":
            return render(request, 'welcome_page.html', {"error": "Sorry Your Account is closed"})

        request.session['contact']=result.contact_no
        request.session['name']=result.name
        request.session['sno']=result.sno
        request.session.set_expiry(0)
        return redirect('view_profile')

    except RegistrationModel.DoesNotExist:
        return render(request,'welcome_page.html',{"error":"Invalid User"})


def view_profile(request):
    sn_o = request.session['sno']
    print(sn_o)
    try:
       profile = ProfileMOdel.objects.get(person__sno=sn_o)
       return render(request,'view_profile.html',{'result':profile})
    except:
        return render(request, 'view_profile.html')


def logout(request):
    del request.session['contact']
    del request.session['name']
    return redirect('main')



def save_industry(request):
    IndustryMOdel(type=request.POST.get("c1")).save()
    success(request, "Industry are saved ")
    return redirect('add_industry')


def validate_profile(request):
    form  = ProfileForm()

    if request.method == 'POST' or request.method == 'FILES':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    return render(request,'validate_profile.html',{'industry':IndustryMOdel.objects.all(),'form':form})


def update_profile(request):
    try:
        sn_o = request.session['sno']
        profile = ProfileMOdel.objects.get(person__sno=sn_o)
        form  = ProfileForm(instance=profile)

        if request.method == 'POST' or request.method == 'FILES':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('view_profile')
    except ProfileMOdel.DoesNotExist:
        return redirect('validate_profile')
    return render(request,'update_profile.html',{'form':form})


def save_Profile(request):
    name=request.POST.get("e5")
    education=request.POST.get("e1")
    image=request.FILES["e2"]
    resume=request.FILES["e3"]
    itype=request.POST.get("e4")
    str=ProfileMOdel(person_id=name,Education=education,photo=image,resume=resume,itype_id=itype).save()
    success(request, "profiles are update succefully ")

    return redirect('view_profile')


def delete_profile(request):
    sn_o = request.session['sno']
    ProfileMOdel.objects.get(person__sno=sn_o).delete()
    return redirect('view_profile')


def about(request):
    return render(request,"about.html")