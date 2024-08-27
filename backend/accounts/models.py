from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None, **extra_fields):
        
        if not email:
            raise ValueError('Users must have an email address')

        if len(email) > 200:
            raise ValueError('Email must be at most 200 characters')
        if len(first_name) > 50:
            raise ValueError('First name must be at most 50 characters')
        if len(last_name) > 100:
            raise ValueError('Last name must be at most 100 characters')
        if len(phone) != 14:
            raise ValueError('Phone must have exactly 14 characters')


        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, phone, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=200, verbose_name='E-mail')
    first_name = models.CharField(max_length=50, blank=False, verbose_name='Nome')
    last_name = models.CharField(max_length=100, blank=False, verbose_name='Sobrenome')
    phone = models.CharField(max_length=14, blank=False, verbose_name='Celular')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email