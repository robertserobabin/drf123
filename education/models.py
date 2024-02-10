from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='пользователь')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_preview = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='lesson/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link_to_the_video = models.URLField(max_length=100, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                                     verbose_name='пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='пользователь')
    is_subscribed = models.BooleanField(default=False, verbose_name='статус подписки')

    def __str__(self):
        return f"{self.user}: {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'