from django.urls import path
from booklist import views

urlpatterns = [
    path('', views.home, name="home"),
]
