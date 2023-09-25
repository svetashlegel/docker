from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Cours(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='articles/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(max_length=500, verbose_name='описание')

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
