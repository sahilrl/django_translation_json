from django.shortcuts import render
from django.http import HttpResponse
import json


def bookform(request):
    return render(request, "books.html", {'form': form})
