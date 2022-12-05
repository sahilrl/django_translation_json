from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language


def home(request):
    if request.LANGUAGE_CODE == 'en':
        print('reading it in english')
    return HttpResponse(request.LANGUAGE_CODE)
