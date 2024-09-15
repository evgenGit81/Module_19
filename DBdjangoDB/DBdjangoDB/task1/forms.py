from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Ваше имя")
    password = forms.CharField(widget=forms.PasswordInput(), label="Введите пароль", min_length=8)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label="Повторите пароль", min_length=8)
    age = forms.CharField(max_length=3, label="Ваш возраст")