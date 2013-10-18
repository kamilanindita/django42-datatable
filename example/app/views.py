#!/usr/bin/env python
# coding: utf-8


from django.shortcuts import render
from app.models import Person
from app.tables import PersonTable

def people(request):
    people = PersonTable(Person.objects.all())
    return render(request, "index.html", {'people': people})

