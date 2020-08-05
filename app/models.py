# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Order(models.Model):
    phone = models.CharField(max_length=20, default='Телефон')
    adress = models.CharField(max_length=100, default='Адрес')
    order = models.TextField(max_length=20000, default='Заказ')
    time = models.CharField(max_length=100, default='Время заказа')

    def __str__(self):
        return self.phone + " " + self.time