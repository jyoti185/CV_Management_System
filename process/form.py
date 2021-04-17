from django import forms
from process .models import *
import random
from process.utils import TextMessage
from process.models import ProfileMOdel

class Registrationform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    def clean_otp(self):
        cno=self.cleaned_data['contact_no']
        otp=self.cleaned_data['otp']
        otp=random.randint(100000,999999)
        message="Welcome to Rms Your OTP is:"+str(otp)
        TextMessage(message,cno)
        return otp


    class Meta:
        model=RegistrationModel
        exclude=('status',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileMOdel
        fields="__all__"


