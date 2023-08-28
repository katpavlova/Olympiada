from django.core.validators import MinLengthValidator
from django.db import models


class Blank(models.Model):
    fio = models.CharField(
        max_length=255,
        verbose_name="ФИО",
        validators=[
            MinLengthValidator(5, 'Введите ФИО минимум 5 символов')
        ],
    )
    education = models.CharField(
        max_length=400,
        verbose_name="Наименование учебного заведения",
    )
    phone = models.CharField(
        max_length=12,
        verbose_name="Телефон",
        validators=[
            MinLengthValidator(11, 'Введите номер телефона')
        ],
    )
    email = models.EmailField(
        verbose_name="E-mail",
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Анкеты"
        verbose_name_plural = "Анкеты"
