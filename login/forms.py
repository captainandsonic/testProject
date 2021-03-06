# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

# class UserForm(forms.Form):
#     username = forms.CharField(label="用户名", max_length=128)
#     password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

# class UserForm(forms.Form):
#     username = forms.CharField(label="用户名", max_length=128)
#     password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class UserForm(forms.Form):
    username = forms.CharField(label=u"用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=u"密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label=u"验证码")



class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label=u"用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=u"密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=u"确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=u"邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label=u'性别', choices=gender)
    captcha = CaptchaField(label=u'验证码')