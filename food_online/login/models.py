from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Login(models.Model):
    COUNTRY = (
        ('S_KOR','SOUTH KOREA'),
        ('US', 'United States'),
        ('CA', 'CANADA'),
    )
    user_name = models.CharField(max_length=30, primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=10, choices=COUNTRY)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.first_name + ", " + self.last_name)