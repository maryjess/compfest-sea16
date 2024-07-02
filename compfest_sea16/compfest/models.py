from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class ServiceType(models.TextChoices):
    HAIRCUTS_STYLING = 'haircuts_styling', 'Haircuts & Styling'
    MANICURE_PEDICURE = 'manicure_pedicure', 'Manicure & Pedicure'
    FACIAL = 'facial', 'Facial Treatment'

class Rating(models.IntegerChoices):
    WORST = 1, '1'
    BAD = 2, '2'
    AVERAGE = 3, '3'
    GOOD = 4, '4'
    BEST = 5, '5'

class Service(models.Model):
    duration = models.DurationField()
    service_type = models.CharField(
        max_length=50,
        choices=ServiceType.choices
    )

    def __str__(self):
        return self.service_type

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Reservation for {self.customer} on {self.date} at {self.time}"

class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rating = models.SmallIntegerField(
        choices=Rating.choices
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