# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Flower
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(Flower)
admin.site.register(Session)
