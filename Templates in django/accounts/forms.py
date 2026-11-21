from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

PASSWORD_MESSAGES = {
    'password_too_short': 'رمز عبور خیلی کوتاه است؛ باید حداقل ۸ کاراکتر باشد.',
    'password_too_common': 'این رمز عبور بیش از حد رایج است؛ رمز دیگری انتخاب کنید.',
    'password_entirely_numeric': 'رمز عبور نباید فقط از عدد تشکیل شده باشد.',
    'password_too_similar': 'رمز عبور بیش از حد شبیه اطلاعات شخصی شماست.',
}


class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150, validators=[User.username_validator])
    email = forms.EmailField()
    password = forms.CharField(strip=False)
    password_confirm = forms.CharField(strip=False)
    terms = forms.BooleanField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('این نام کاربری قبلاً گرفته شده است.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email

    def clean(self):
        cleaned = super().clean()
        password = cleaned.get('password')
        confirm = cleaned.get('password_confirm')
        if password and confirm:
            if password != confirm:
                self.add_error('password_confirm', 'رمز عبور و تکرار آن یکسان نیستند.')
            else:
                try:
                    validate_password(password)
                except ValidationError as error:
                    for item in error.error_list:
                        self.add_error('password', PASSWORD_MESSAGES.get(item.code, item))
        return cleaned

    def save(self):
        first_name, _, last_name = self.cleaned_data['full_name'].strip().partition(' ')
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=first_name,
            last_name=last_name.strip(),
        )