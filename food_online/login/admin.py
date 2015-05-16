from django.contrib import admin

# Register your models here.
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    class Meta:
        model = Login
        
admin.site.register(Login, LoginAdmin)
    #code