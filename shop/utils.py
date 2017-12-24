# -*- coding: utf-8 -*-
from .models import Flower
from cart.cart import Cart



def is_digit(string):
    if string.isdigit():
       return 1
    else:
        try:
            float(string)
            return None
        except ValueError:
            return None



#def get_lang(request):
  #if request.COOKIES.get('django_language') == 'en':
     #pk = 'english'
     #return 1
  #elif request.COOKIES.get('django_language') == 'uk':
     #pk = 2
     #return pk
  #else:
     #pk = 2
     #return pk
