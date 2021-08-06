from django.db import models
from django.contrib.auth.models import User
 #Create your models here.

class Service(models.Model):
     """Model defninition for Service."""

     name = models.TextField('Service Name')
     user=models.ForeignKey(User,on_delete=models.CASCADE)


     def __str__(self):
         """Unicode representation of Service."""
         return f'{self.name}'

     class Meta:
         verbose_name = 'Service'
         verbose_name_plural = 'Services'

class SubService(models.Model):
    """Model defninition for SubService."""

    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    name = models.TextField('Sub Service')

    def __str__(self):
        """Unicode representation of SubService."""
        return '{0}:{1}'.format(self.service, self.name)

class SubTime(models.Model):

    """Model defninition for SubTime."""
    servicename=models.ForeignKey('Service',on_delete=models.CASCADE,blank=True,null=True)
    subservice=models.ForeignKey('SubService',on_delete=models.CASCADE,blank=True,null=True)
    TimeSlot=models.TextField()
    Date=models.TextField()

    def __str__(self):
        """Unicode representation of SubTime."""
       # return f'{self.subservice}'
        return '{0}:{1}'.format(self.servicename, self.subservice)

class Booking(models.Model):
    PENDING = 1
    APPROVED = 2
    STATUSES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.IntegerField(choices = STATUSES)
    time_of_result = models.DateTimeField()

class BookingLine(models.Model):
    booking = models.ForeignKey('Booking', on_delete = models.CASCADE)
    service = models.ForeignKey('Service', on_delete = models.CASCADE)

