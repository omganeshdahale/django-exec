from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    demo = Demo.objects.create(title="Demo")
    demo = Demo.objects.get(pk=demo.pk)
    return JsonResponse({"message": "Done"})
