from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer
# from .models import User, Review

# TODO jadi pakainya myuser nih, bukan customer?
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

# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['avatar', 'name', 'username', 'email', 'bio']
        # TODO add avatar for user
        fields = ['first_name', 'last_name', 'email']

# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'
#         exclude = ['host', 'participants']

# class ReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = ['first']
