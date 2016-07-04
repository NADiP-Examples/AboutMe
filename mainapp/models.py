from django.db import models


# class Work(models.Model):
#     organization = models.CharField(verbose_name='Организация', max_length=32)
#     region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
#     site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
#     position = models.CharField(verbose_name='Должность', max_length=16)
#     duties = models.TextField(verbose_name='Обязанности')
#     period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Organization(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32,
                            unique=True)
    region = models.CharField(verbose_name='Регион', max_length=32)
    site = models.CharField(verbose_name='Сайт', max_length=64,
                            blank=True)
    tax_id = models.IntegerField(verbose_name='ИНН')


class Work(models.Model):
    organization = models.ForeignKey(Organization,
            verbose_name='Организация')
    #  organization = models.ForeignKey('Organization', verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', unique=True, max_length=32)


class Study(models.Model):
    type = models.CharField(verbose_name='Тип заведения', max_length=16)
    number = models.PositiveIntegerField(verbose_name='Номер заведения')
    address = models.CharField(verbose_name='Адрес', default='no_address', max_length=32)
    study_from = models.DateField(verbose_name='Учился с')
    study_to = models.DateField(verbose_name='Учился до')
