from django.db import models
from django.contrib import admin
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args,**kwargs)
    
    class Meta:
        managed=False

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
