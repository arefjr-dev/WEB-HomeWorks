from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from .forms import RegisterForm


@never_cache
def login_view(request):
    if request.method == 'POST':
        # منطق ورود واقعی در این تمرین خواسته نشده؛ فقط صفحه دوباره باز می‌شود
        return redirect('/login/')
    return render(request, 'accounts/login.html')


@never_cache
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد. اکنون می‌توانید وارد شوید.')
            return redirect('/login/')

        for errors in form.errors.values():
            for error in errors:
                messages.error(request, error)
        # نوشته‌های کاربر (به‌جز رمزها) را برای نمایش بعد از redirect نگه می‌داریم
        request.session['register_values'] = {
            'full_name': request.POST.get('full_name', ''),
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
        }
        return redirect('/register/')

    values = request.session.pop('register_values', {})
    return render(request, 'accounts/register.html', {'values': values})