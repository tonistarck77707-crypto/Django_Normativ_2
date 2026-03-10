from django import forms
from .models import Product
#from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'author', 'price']
#        fields = "__all__"

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Parollar bir xil emas!")

        return cleaned_data

    class LoginForm(forms.Form):
        username = forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)

        def clean(self):
            cleaned_data = super().clean()
            username = cleaned_data.get("username")
            password = cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if not user:
                raise ValidationError("Username yoki parol noto‘g‘ri!")

            cleaned_data['user'] = user
            return cleaned_data

