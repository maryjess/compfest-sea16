# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.email

class UserType(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    ADMIN = 'admin', 'Admin'

class ServiceType(models.TextChoices):
    HAIRCUTS_STYLING = 'haircuts_styling', 'Haircut and Styling'
    MANICURE_PEDICURE = 'manicure_pedicure', 'Manicure and Pedicure'
    FACIAL = 'facial', 'Facial Treatment'

class Rating(models.IntegerChoices):
    WORST = 1, '1'
    BAD = 2, '2'
    AVERAGE = 3, '3'
    GOOD = 4, '4'
    BEST = 5, '5'

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    type = models.CharField(
        max_length = 8,
        choices = UserType.choices,
        default = UserType.CUSTOMER,
    )
    # TODO password will be configured during authentication (django auth)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Admin(User):
    is_admin = models.BooleanField(False)
    type = UserType.ADMIN

class Customer(User):
    # TODO think whether is_admin is better,
    # or whether using enumeration is better
    is_admin = models.BooleanField(False)
    type = UserType.CUSTOMER

class Service(models.Model):
    duration = models.DurationField()
    service_type = models.CharField(
        max_length = 20,
        choices = ServiceType.choices
    )

    def __str__(self):
        return self.service_type

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.service} reservation for {self.customer} on {self.date} at {self.time}"

class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rating = models.SmallIntegerField(
        choices = Rating.choices
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} reviewed {self.rating} on {self.created_at}"

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"SEA Salon Branch {self.name} at {self.location}"