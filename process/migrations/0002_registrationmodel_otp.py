# Generated by Django 3.1.2 on 2020-12-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='otp',
            field=models.IntegerField(default=None),
        ),
    ]
