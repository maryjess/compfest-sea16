from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = False  # ensure is_admin is set to False for customers
        # user.type = 'customer' # explicitly set type to customer
        if commit:
            user.save()
        return user

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['avatar', 'name', 'email']
        # TODO add avatar for user
        fields = ['first_name', 'last_name', 'email']

class ReservationForm(forms.Form):
    SERVICE_CHOICES = [
        ('haircuts_styling', 'Haircuts & Styling'),
        ('manicure_pedicure', 'Manicure & Pedicure'),
        ('facial_treatments', 'Facial Treatments')
    ]

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    service_type = forms.ChoiceField(choices=SERVICE_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
