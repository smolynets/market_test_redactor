# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Flower
from .cart import Cart
from .forms import CartAddProductForm
from .models import Order, OrderItem
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def CartAdd(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.add(flower=flower, quantity=1)
    return redirect('main')

#######################################################################



def basket(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item
                                               ['quantity'],
                                            'update': True
                                        })
    return render(request, 'shop/basket.html', {'cart': cart})

#####################################################################


def CartAdd_basket(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(flower=flower, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('basket')

#########################################################################

def CartRemove(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.remove(flower)
    return redirect('basket')





#########################################################################

def CartRemove_main_page(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.remove(flower)
    return redirect('main')


#############################################################################



def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        errors = {}
        data = {}

        # validate user input
        name = request.POST.get('name', '').strip()
        if not name:
          errors['name'] = u"Ім'я є обов'язковим"
        else:
          data['name'] = name

        number = request.POST.get('number', '').strip()
        if not number:
          errors['number'] = u"Номер телефону є обов'язковим"
        else:
          data['number'] = number

        notes = request.POST.get('notes', '').strip()
        if notes:
          data['notes'] = notes
        
        total_cost = request.POST.get('total_cost', '').strip()
        data['total_cost'] = total_cost
        
        if not errors:
          order = Order(**data)
          order.save()
          for item in cart:
            OrderItem.objects.create(order=order, product=item['flower'],
                                         price=item['price'],
                                         quantity=item['quantity'])
          cart.clear()
          return HttpResponseRedirect( u'%s?status_message=Замовлення успішно збережено!' 
              % reverse('main'))
        else:
          return render(request, 'shop/ordering.html',
            {'errors': errors})

    return render(request, 'shop/ordering.html', {'cart': cart})


#####################################################################








def orders(request):
  orders = Order.objects.all()
  return render(request, 'shop/orders.html', {'orders': orders})




#########################################################################






def one_order(request, pk):
  order = Order.objects.get(pk=pk)
  products = OrderItem.objects.filter(order=order)
  return render(request, 'shop/one_order.html', {'order':order, 
    'products': products})




###############################################################################
