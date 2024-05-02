from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=64, help_text="Введите название компании", verbose_name="Название компании")
    info = models.CharField(max_length=64, help_text="Введите информацию", verbose_name="Информация")

    class Meta:
        verbose_name_plural = "Производитель"
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    organization = models.ForeignKey(Organization,
                                     on_delete=models.CASCADE,
                                     null=True)

    patronymic = models.CharField(max_length=150, blank=True)

    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = "Профиль"

    def __str__(self):
        return f'Profile of {self.user.username}'
