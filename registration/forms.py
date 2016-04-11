# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.forms import CharField, Form, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile


from django import forms


from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserC


class RegForm(forms.ModelForm):
    username2 = forms.CharField(max_length = 30,label = 'Ник')
    firstname = forms.CharField(label='Имя', max_length = 30, required = False )
    lastname = forms.CharField( label='Фамилия',max_length = 30, required = False )
    email = forms.CharField(label='Почта', max_length = 30 )
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput, min_length = 6, max_length = 30 )
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        # TODO: проверить, что username не занят
        return self.cleaned_data

    def clean_password(self):
    	
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # TODO: проверить, что пароли совпадают
        return self.cleaned_data
    class Meta:
    	model = User
    	fields = ('username2',)

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(label='Телефон',max_length=20)
	birth_date = forms.DateField(label='Дата Рождения') 
	
	class Meta:
		model = UserProfile
		fields = ('phone',)

    	
	     
    


    
    


