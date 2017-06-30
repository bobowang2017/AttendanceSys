# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Test(models.Model):
    test_id = models.CharField(max_length=64, verbose_name=u'number', primary_key=True)

    class Meta:
        verbose_name = u'Test'
        verbose_name_plural = verbose_name
        db_table = 'test'

    def __unicode__(self):
        return self
