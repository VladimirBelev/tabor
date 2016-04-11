# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User




# Create your views here.
from .forms import  RegForm, UserProfileForm
from .models import UserProfile



def registrate(reguest):
	user =User()
	userProfile = UserProfile()
	if reguest.POST:
		form =  RegForm(reguest.POST, instance = user)
		userProfileForm = UserProfileForm( reguest.POST, instance = userProfile )
		if form.is_valid() and userProfileForm.is_valid():
			userData = form.cleaned_data
			user.username = userData['username2']
			user.first_name = userData['firstname']
			user.last_name = userData['lastname']
			user.email = userData['email']      		
			user.set_password( userData['password1'])
			user.save()

			
			userProfileData = userProfileForm.cleaned_data
			userProfile.phone = userProfileData['phone']
			userProfile.dob = userProfileData['birth_date']
			userProfile.save()

			return HttpResponse('Форма верна')

	else:
		form =  RegForm()
		userProfileForm = UserProfileForm( )
	return render(reguest, 'registrate.html',{'form': form, 'form2': userProfileForm})

