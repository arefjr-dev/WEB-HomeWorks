from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'action', 'اکشن'
        DRAMA = 'drama', 'درام'
        COMEDY = 'comedy', 'کمدی'
        HORROR = 'horror', 'ترسناک'
        SCIFI = 'scifi', 'علمی‌تخیلی'
        THRILLER = 'thriller', 'هیجان‌انگیز'
        ROMANCE = 'romance', 'عاشقانه'
        ANIMATION = 'animation', 'انیمیشن'
        DOCUMENTARY = 'documentary', 'مستند'

    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='خلاصه داستان')
    genre = models.CharField(max_length=20, choices=Genre.choices, verbose_name='ژانر')
    release_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(2026)],
        verbose_name='سال ساخت',
    )
    duration_minutes = models.PositiveSmallIntegerField(verbose_name='مدت (دقیقه)')
    director = models.CharField(max_length=100, verbose_name='کارگردان')
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='امتیاز (از ۱۰)',
    )
    is_series = models.BooleanField(default=False, verbose_name='سریال است')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')

    class Meta:
        db_table = 'movie'
        ordering = ['-created_at']
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم‌ها'

    def __str__(self):
        return f'{self.title} ({self.release_year})'