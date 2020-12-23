from django.shortcuts import render,redirect
from process.form import Registrationform
from django.contrib.messages import success
from process.models import RegistrationModel


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



def confirmation(request):

    return render(request,"confirmation.html")


def welcome_page(request):
    return render(request,"welcome_page.html")


def validate_login(request):
    try:
        result=RegistrationModel.objects.get(Email_id=request.POST.get('u1'),password=request.POST.get('u2'))
        if result.status=="Pending":
            return render(request, 'welcome_page.html', {"error": "Sorry Your Registration is Pending"})
        if result.status=="closed":
            return render(request, 'welcome_page.html', {"error": "Sorry Your Account is closed"})

        request.session['contact']=result.contact_no
        request.session['name']=result.name
        return redirect('view_profile')

    except RegistrationModel.DoesNotExist:
        return render(request,'welcome_page.html',{"error":"Invalid User"})


def view_profile(request):
    return render(request,'view_profile.html')


def logout(request):
    del request.session['contact']
    del request.session['name']
    return redirect('main')