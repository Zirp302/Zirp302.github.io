from django.urls import path
from . import views

urlpatterns = [             #оброщение к индексам в папке views.py
    path('', views.index),
    path('portfolio', views.portfolio),
    path('my', views.my),
    path('blog', views.blog),
    path('kontakt', views.kontakt)
]