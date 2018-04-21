# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Property(models.Model):
    prop_type = models.CharField(max_length=48)
    picture_url = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    nearest_elementary = models.CharField(max_length=256)


    zip_code = models.IntegerField(null=True)


