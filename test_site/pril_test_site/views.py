from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pril_test_site/test_hablon.html')

def portfolio(request):
    return render(request, 'pril_test_site/test_hablon_portfolio.html')

def my(request):
    return render(request, 'pril_test_site/test_hablon_my.html')

def blog(request):
    return render(request, 'pril_test_site/test_hablon_blog.html')

def kontakt(request):
    return render(request, 'pril_test_site/test_hablon_kontakt.html')


