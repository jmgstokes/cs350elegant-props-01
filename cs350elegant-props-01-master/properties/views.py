# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .models import Property


# Show the all the properties in the db.

class PropertyListView(generic.ListView):
    model = Property
    template_name = "properties/list.html"

class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = "properties/detail.html"

