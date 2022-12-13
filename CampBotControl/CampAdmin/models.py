from django.db import models

from django.db import models


class Users(models.Model):
    user_id = models.BigIntegerField(verbose_name='id telegram', unique=True)
    date_reg = models.DateTimeField(
        auto_now_add=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    department = models.IntegerField(default=99)
    admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class TypeEducation(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тип обучения')
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name = 'Тип обучения'
        verbose_name_plural = 'Типы обучения'


class Faculties(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя Факультета')
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Profile(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя направления')
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        unique_together = ['name']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Data(models.Model):
    descriptions = models.TextField(verbose_name='Описание образования')
    type_education = models.ForeignKey(
        TypeEducation,
        on_delete=models.CASCADE,
        related_name='educations',
        verbose_name='типы образования',
    )
    faculties = models.ForeignKey(
        Faculties,
        on_delete=models.CASCADE,
        related_name='faculties',
        verbose_name='факультеты',
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profiles',
        verbose_name='профили',
    )
    def __str__(self) -> str:
        return f'{self.type_education} {self.faculties} {self.profile}'
    class Meta:
        unique_together = ['type_education', 'faculties', 'profile']
        verbose_name = 'Описание профиля'
        verbose_name_plural = 'Описание профилей'
