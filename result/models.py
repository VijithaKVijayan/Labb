from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    POSITIVE = 1
    NEGATIVE = 2
    RESULTS = (
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (None, 'None'),
    )
    result_pdf = models.FileField('Result File', upload_to='documents/%Y/%m/%d', null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete = models.CASCADE)
    value = models.IntegerField()
    result = models.IntegerField(choices = RESULTS, blank = True, null = True)

    def __str__(self):
        if self.result:
            if self.result == self.POSITIVE:
                r = 'Positive'
            else:
                r = 'Negative'
            return f'{self.user.username}: {self.service.name}: {r}'
        return f'{self.user.username}: {self.service.name}: {self.value}'
            

class ResultUpload(models.Model):
    resultfile = models.FileField('Result File',upload_to='documents/%Y/%m/%d')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Result."""
        return f'{self.result_file}'