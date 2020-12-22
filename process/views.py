from django.shortcuts import render,redirect
from process.form import Registrationform
from django.contrib.messages import success


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