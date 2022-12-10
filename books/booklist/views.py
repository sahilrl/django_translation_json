from django.shortcuts import render

def bookform(request):
    return render(request, "books.html")
