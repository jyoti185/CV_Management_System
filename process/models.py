from django.db import models

class IndustryMOdel(models.Model):
    sno=models.AutoField(primary_key=True)
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.type


class RegistrationModel(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contact_no=models.IntegerField(unique=True)
    Email_id=models.CharField(unique=True,max_length=100)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=None)
    status=models.CharField(max_length=20,default='Pending')

    Date_of_join=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProfileMOdel(models.Model):
    sno = models.AutoField(primary_key=True)
    person=models.OneToOneField(RegistrationModel,on_delete=models.CASCADE)
    Education=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="user_image/")
    resume=models.FileField(upload_to="user_resume/")
    itype=models.ForeignKey(IndustryMOdel,on_delete=models.CASCADE)


# Create your models here.
