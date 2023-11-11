import uuid
from django.db import models


class Attraction(models.Model):
    def get_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex
        return f'attractions/covers/{image_uuid}.{extension}'
    
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(max_length=255, verbose_name='Категория')
    cover = models.ImageField(blank=True, null=True, upload_to=get_path, verbose_name='Баннер')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    lat = models.CharField(max_length=255, verbose_name='Широта')
    lon = models.CharField(max_length=255, verbose_name='Долгота')
    musculoskeletal_disorders = models.BooleanField(blank=True, null=True, verbose_name='Нарушения опорно-двигательного аппарата')
    visual_impairment = models.BooleanField(blank=True, null=True, verbose_name='Нарушения зрения')
    hearing_impairment = models.BooleanField(blank=True, null=True, verbose_name='Нарушения слуха')
    intellectual_impairment = models.BooleanField(blank=True, null=True, verbose_name='Нарушения интеллекта')

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'