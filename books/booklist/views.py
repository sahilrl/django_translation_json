from django.shortcuts import render
from django.http import HttpResponse
from booklist.forms import BooksForm
import json


def bookform(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            store_cleaned_data = {}
            for i in form.fields:
                store_cleaned_data[i] = form.cleaned_data[i]
            print(store_cleaned_data)
            store_cleaned_data = json.dumps(store_cleaned_data)
            print(store_cleaned_data)
        return HttpResponse('successs')
    form = BooksForm()
    return render(request, "books.html", {'form': form})
