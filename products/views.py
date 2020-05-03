from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def index(request):
    return HttpResponse("Learning Django MotherFucker!!!")


def new_products(request):
    return HttpResponse("this is the place where you see the new products")