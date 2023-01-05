from django.db import models


class Student(models.Model):

    GENDER_CHOOICES = (
        ('M', 'M'),
        ('W', 'W'),
    )

    first_name = models.CharField(
        verbose_name='имя студента',
        max_length=100,
        )
    surname = models.CharField(
        verbose_name='фамилия студента',
        max_length=150
    )
    gender = models.CharField(
        choices=GENDER_CHOOICES, #выборка
        max_length=1
    )
    is_frozen = models.BooleanField(default=False)

