from django.db import models
class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    zip = models.CharField(max_length=100, blank=True, default='')
    id=models.AutoField(primary_key=True)
   
    def _str_(self):
       return(f'{self.first_name} {self.last_name}')
        

