# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Investor(models.Model):
    account_name = models.CharField()
    username = models.CharField()
    password = models.CharField()
    deposit = models.CharField()

class Company(models.Model):
    company_name = models.CharField()
    description = models.CharField()
    budget = models.IntegerField()
    basic_info = models.CharField()
    financial_info = models.CharField()
    extra_info = models.CharField()


