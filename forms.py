from django import forms
from .models import Mentor, Groupv, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary", "photo"]


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groupv
        fields = ["specification", "block", "time", "language", "name", "mentor", "student_qty", "status"] 


# class StudentCreateForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary"]      


class createuserform(UserCreationForm):
     class Meta:
         model= User
         fields = ['username' , 'email' , 'password1', 'password2']
         
     