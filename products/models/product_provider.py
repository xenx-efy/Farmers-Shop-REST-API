from django.contrib import admin
from django.db import models

from config import settings


class ProductProvider(models.Model):
    phone = models.CharField(max_length=255)
    description = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @admin.display(ordering="user__first_name")
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering="user__last_name")
    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return f'{self.first_name()} {self.last_name()}'

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
