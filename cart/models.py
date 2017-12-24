# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.models import Flower



class Order(models.Model):

	class Meta(object):
		verbose_name = u'Замовлення'
		verbose_name_plural = u'Замовлення'

	name = models.CharField(
      max_length=256,
      blank=False)
	number = models.CharField(
      max_length=256,
      blank=False)
	notes = models.TextField(
      blank=True)
	total_cost = models.CharField(
    max_length=256,
	  blank=False)
	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

	def __unicode__(self):
		return u'%s' % (self.name)






class OrderItem(models.Model):
    order = models.ForeignKey(Order,
     related_name='items')
    product = models.ForeignKey(Flower,
     related_name='order_items')
    price = models.DecimalField(
    	verbose_name='Ціна',
    	max_digits=10,
    	decimal_places=4)
    quantity = models.PositiveIntegerField(
    	verbose_name='Кількість',
    	default=1)
    def get_cost(self):
    	return self.price * self.quantity
    def __unicode__(self):
        return u'%s' % (self.order)
