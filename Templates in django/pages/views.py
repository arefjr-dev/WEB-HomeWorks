from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد. به‌زودی پاسخ می‌دهیم.')
        else:
            messages.error(request, 'اطلاعات واردشده معتبر نیست. لطفاً دوباره بررسی کنید.')
        return redirect('/contact/')
    return render(request, 'pages/contact.html')