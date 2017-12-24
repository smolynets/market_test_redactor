# -*- coding: utf-8 -*-
from __future__ import print_function

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from PIL import Image
from django.utils.translation import ugettext as _







def users_list(request):
	users = User.objects.all()
	return render(request, 'users_list.html',
    {'users': users})







def users_one(request, pk):
   use = User.objects.get(id=pk)
   return render(request, 'user_one_profile.html',
   {'user_one': use})










def user_one_edit(request, pk):
    use = User.objects.get(pk=pk)
    
    
    if request.method == "POST":
      data = User.objects.get(pk=pk)
      ln = User.objects.get(pk=pk)
      if request.POST.get('add_button') is not None:

        errors = {}

        username = request.POST.get('username', '').strip()
        if not username:
          errors['username'] = _(u"імя є обовязковим.")
        else:
          data.username = username

        password = request.POST.get('password', '').strip()
        if not password:
          errors['password'] = _(u"пароль є обовязковим.")
        else:
          data.password = password

        email = request.POST.get('email', '').strip()
        if not email:
          errors['email'] = "пошта є обовязковою."
        else:
          data.email = email

        lang = request.POST.get('lang', '').strip()
        if not lang:
          errors['lang'] = "мова є обовязковою"
        else:
          ln.stprofile.lang = lang


        if not errors:
          
          data.save()
          ln.stprofile.save()
          print(ln)
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('users_list'), _(u'користувач успішно відредагований')))
        else:
          # render form with errors and previous user input
          return render(request, 'user_edit.html',
          {'pk': pk,'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('users_list'), _('редагування користувача відмінено')))
    else:
     # initial form render
     return render(request, 'user_one_edit.html',
     {'use': use, 'pk': pk})









def user_e(request, pk):
    use = User.objects.get(pk=pk)
    
    
    if request.method == "POST":
      ln = User.objects.get(pk=pk)
      print(ln)
      if request.POST.get('add_button') is not None:

        errors = {}

        lang = request.POST.get('lang', '').strip()
        if not lang:
          errors['lang'] = _(u"мова є обовязковою")
        else:
          ln.stprofile.lang = lang


        if not errors:
          
          ln.stprofile.save()
          print(ln)
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('users_list'), _(u'користувач успішно відредагований')))
        else:
          # render form with errors and previous user input
          return render(request, 'user_edit.html',
          {'pk': pk,'errors': errors})
      elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('users_list'), _('редагування користувача відмінено')))
    else:
     # initial form render
     return render(request, 'user_one_edit.html',
     {})
