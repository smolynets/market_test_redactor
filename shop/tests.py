# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.from datetime import datetime

from django.test import TestCase
from django.http import HttpRequest

from shop.models import Flower
from shop.utils import is_digit

class UtilsTestCase(TestCase):
    """Test functions from util module"""

    def setUp(self):
        # create 2 groups
        group1, created = Group.objects.get_or_create(
            id=1,
            title="Group1")
        group2, created = Group.objects.get_or_create(
            id=2,
            title="Group2")

        # create student
        student, created = Student.objects.get_or_create(
            id=1,
            first_name="Vitaliy",
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='12345')
        
        # set student as leader for group1
        group1.leader = student
        group1.save()

    