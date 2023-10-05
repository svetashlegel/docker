from django.db import models
from config import settings
from django.utils.timezone import now

NULLABLE = {'blank': True, 'null': True}


class Cours(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='articles/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(max_length=500, verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='articles/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(max_length=500, verbose_name='описание')
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')
    date = models.DateField(default=now, verbose_name='дата оплаты')
    summ = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, verbose_name='способ оплаты', default='non-cash')

    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')


class Subscription(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, verbose_name='курс')
    is_active = models.BooleanField(verbose_name='активирована', default=True)
