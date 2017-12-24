# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import Flower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import is_digit
from cart.cart import Cart
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView




###########################################################################
def main_page(request):
  flowers = Flower.objects.get_queryset().order_by('id')
  # try to order flowers list
  order_by = request.GET.get('order_by', '')
  if order_by in ('price', '#'):
    flowers = flowers.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
      flowers = flowers.reverse()
  #pagination
  paginator = Paginator(flowers, 4)
  page = request.GET.get('page')
  try:
    flowers = paginator.page(page)
  except PageNotAnInteger:
    flowers = paginator.page(1)
  except EmptyPage:
    flowers= paginator.page(paginator.num_pages)
  #cart indicator(main page)
  list = []
  cart = Cart(request) 
  for item in cart:
    list.append(item['flower'])
  cart_main = list 
  return render(request, 'shop/main.html', {'flowers':flowers,
    'cart_main':cart_main})





#########################################################################
#flower_add

def flower_add(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for student object
      data = {}
      # validate user input
      title = request.POST.get('title', '').strip()
      if not title:
        errors['title'] = u"Ім'я є обов'язковим"
      else:
        data['title'] = title

        
        
      price = request.POST.get('price', '').strip()
      if not price:
          errors['price'] = u"Ціна є обов'язковою"
      else:
          if is_digit(price) == 1:
            data['price'] = price
          else:
            errors['price'] = u"Введіть ціле число!"
      description = request.POST.get('description', '').strip()
      if not description:
        errors['description'] = u"Опис є обов'язковим"
      else:
        data['description'] = description  
      photo_main = request.FILES.get('photo_main')
      if not photo_main:
        errors['photo_main'] = u"Одне фото є обов'язковим"
      else:
        data['photo_main'] = photo_main 
      photo_big = request.FILES.get('photo_big')
      if photo_big:
        data['photo_big'] = photo_big 
      data['user'] = request.user

           
      # save flovwer
      if not errors:
        flower = Flower(**data)
        flower.save()
        # redirect to students list
        return HttpResponseRedirect( u'%s?status_message=Квітку успішно додано!'  % reverse('main'))
      else:
        # render form with errors and previous user input
        return render(request, 'shop/flower_add.html',
        {'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=Додавання квітки скасовано!' % reverse('main'))
  else:
   # initial form render
   return render(request, 'shop/flower_add.html', {})





#####################################################################
def one_flower(request, pk):
  flower = Flower.objects.filter(pk=pk)
  return render(request, 'shop/one_flower.html', {'flower':flower})






#####################################################################
#flower_edit


def flower_edit(request, pk):
    flower = Flower.objects.filter(pk=pk)

    
    if request.method == "POST":
        data = Flower.objects.get(pk=pk)
        if request.POST.get('add_button') is not None:
            
            errors = {}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Імʼя є обовʼязковим."
            else:
                data.title = title

            price = request.POST.get('price', '').strip()
            if not price:
               errors['price'] = u"Ціна є обов'язковою"
            else:
               if is_digit(price) == 1:
                 data.price = price 
               else:
                 errors['price'] = u"Введіть ціле число!"

            description = request.POST.get('description', '').strip()
            if not description:
               errors['description'] = u"Опис є обов'язковим"
            else:
               data.description = description

            photo_main = request.FILES.get('photo_main')
            if photo_main:
                data.photo_main = photo_main  
                  
            photo_big = request.FILES.get('photo_big')
            if photo_big:
               data.photo_big = photo_big 


            if errors:
                return render(request, 'shop/flower_edit.html', {'pk': pk, 'flower': data, 'errors': errors})
            else:
                data.save()
                return HttpResponseRedirect(u'%s?status_message=Редагування квітки  завершено' % reverse('main'))
        elif request.POST.get('cancel_button') is not None:

            return HttpResponseRedirect(u'%s?status_message=Редагування квітки скасовано!' % reverse('main'))
        
    else:
        return render(request,
                      'shop/flower_edit.html', {'pk': pk, 'flower': flower[0]})
                      






########################################

#flower delete

class FlowerDelete(DeleteView):
  model = Flower
  template_name = 'shop/flower_delete.html'
  def get_success_url(self):
    return u'%s?status_message=Квітку успішно видалено!' % reverse('main')
  def post(self, request, *args, **kwargs):
    if request.POST.get('no_delete_button'):
      return HttpResponseRedirect(u'%s?status_message=Видалення  квітки відмінено!'% reverse('main'))
    else:
      return super(FlowerDelete, self).post(request, *args, **kwargs)


#################################################################


def search(request):
  title = request.POST.get('search', '').strip()
  if not title:
    return render(request, 'shop/no_search.html', {})
  flw = Flower.objects.filter(title=title)
  if flw:
    return render(request, 'shop/one_flower.html', {'flower':flw })
  else:
    return render(request, 'shop/no_one_flower.html', {})

