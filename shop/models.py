# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Flower(models.Model):

	class Meta(object):
		verbose_name = u'Квітка'
		verbose_name_plural = u'Квіти'

	title = models.CharField(
      max_length=256,
      blank=False)
	price = models.CharField(
      max_length=256,
      blank=False)
	description = models.TextField(
      blank=False)
	photo_main = models.ImageField(
      blank=False,
      null=False)
	photo_big = models.ImageField(
      blank=True,
      null=True)
	user = models.CharField(
      max_length=256,
      blank=False)
	def __unicode__(self):
		return u'%s' % (self.title)