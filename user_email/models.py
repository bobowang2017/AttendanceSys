# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Email(models.Model):
    EMAIL_STATUS = (
        (0, u'未读'),
        (1, u'已读'),
        (-1, u'删除')
    )
    email_id = models.CharField(max_length=64, verbose_name=u'序号', primary_key=True)
    email_sender = models.CharField(max_length=64, verbose_name=u'发送者')
    email_receiver = models.CharField(max_length=64, verbose_name=u'接受者')
    email_title = models.CharField(max_length=256, verbose_name=u'邮件主题')
    email_content = models.TextField(verbose_name=u'邮件内容')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name=u'邮件发送时间')
    email_status = models.IntegerField(choices=EMAIL_STATUS, default=0)

    class Meta:
        verbose_name = u'邮件表'
        verbose_name_plural = verbose_name
        db_table = 'email'

    def __unicode__(self):
        return self
