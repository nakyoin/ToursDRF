from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import related


class Tour(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    peoples = models.IntegerField()
    place = models.CharField(max_length=100)
    excource = models.ForeignKey('Excourses', on_delete=models.CASCADE)
    priceoftour = models.IntegerField()

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


    def __str__(self):
        return self.name



class Countries(models.Model):
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country



class Excourses(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'

    def __str__(self):
        return self.name


class Profile(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    price = models.IntegerField()
    time_start = models.TimeField()
    time_end = models.TimeField()


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.tour)