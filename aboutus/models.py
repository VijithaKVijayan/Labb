from django.db import models

# Create your models here.
class Home(models.Model):
    description=models.TextField('Home Description')
    contactdetail=models.TextField('Contcat Us')

class Aboutus(models.Model):
    description=models.TextField('About Us')

class HomeImage(models.Model):
    home=models.ForeignKey('Home',on_delete=models.CASCADE)
    #images=models.FileField(upload_to='documents/%Y/%m/%d')

class AboutUsImage(models.Model):
    aboutus=models.ForeignKey('Aboutus',on_delete=models.CASCADE)
    #ges=models.FileField(upload_to='documents/%Y/%m/%d')