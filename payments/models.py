from django.db import models
from education.models import Course, Lesson
from user.models import User

NULLABLE = {'blank': True, 'null': True}

STATUS_CHOICES = [
    ('card', 'card'),
    ('cash', 'cash'),
]

class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                             related_name='payments', verbose_name='пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    amount = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=STATUS_CHOICES,
                                      verbose_name='способ оплаты')
    course_payment = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE,
                                       related_name='payments', verbose_name='оплаченный курс')
    lesson_payment = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE,
                                       related_name='payments', verbose_name='оплаченный урок')
    session_id = models.CharField(max_length=150, verbose_name='id сессии', **NULLABLE)
    is_paid = models.BooleanField(default=False, verbose_name='статус оплаты')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ['-date']