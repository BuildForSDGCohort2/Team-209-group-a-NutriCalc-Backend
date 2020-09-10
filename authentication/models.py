from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin

# Create your models here.

# Custom User model for verify user emails and sending verification links
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError('Users should have a unique username')
        if email  is None:
            raise TypeError('Users should have a unique email')
        
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email,password):
        if password is None:
            raise TypeError('Users should have password')

        user=create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user


class User(AbstractUser):
    username=models.CharField(max_length=255,unique=True, db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username-self.email
    def tokens(self):
        return ''