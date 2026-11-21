from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def login_view(request):
    return render(request, 'pages/login.html')


def register(request):
    return render(request, 'pages/register.html')