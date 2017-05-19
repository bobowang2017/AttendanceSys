# -*- coding: utf-8 -*-
import uuid

from django.core.mail import send_mail
from AttendanceSys.settings import DEFAULT_FROM_EMAIL
from serializer import EmailSerializer, Email
from common.decorator import filter_none_param


def send_email(receiver_list, header, content):
    receivers = receiver_list.split(';')
    send_status = send_mail(header, content, DEFAULT_FROM_EMAIL, receivers)
    if send_status:
        email_id = str(uuid.uuid5(uuid.uuid4(), str(uuid.uuid4())))
        create_email(email_id=email_id, email_sender=DEFAULT_FROM_EMAIL,
                     email_receiver=receivers[0], email_title=header, email_content=content)
    return 1 if send_status else 0


@filter_none_param
def create_email(**kwargs):
    serializer = EmailSerializer(data=kwargs)
    if serializer.is_valid(raise_exception=True):
        serializer.save(**kwargs)


@filter_none_param
def get_email(page_num, page_size, **kwargs):
    start = (page_num-1) * page_size
    end = start + page_size
    result = Email.objects
    if kwargs.get('email_title'):
        email_title = kwargs.get('email_title')
        kwargs.pop('email_title')
        result = result.filter(email_title__contains=email_title)
    if kwargs.get('email_receiver'):
        email_receiver = kwargs.get('email_receiver')
        kwargs.pop('email_receiver')
        result = result.filter(email_receiver__contains=email_receiver)

    # if kwargs.get('user_name'):
    #     user_name = kwargs.get('user_name')
    #     kwargs.pop('user_name')
    #     result = result.filter(user_name__contains=user_name)
    # if kwargs.get('user_phone'):
    #     user_phone = kwargs.get('user_phone')
    #     kwargs.pop('user_phone')
    #     result = result.filter(user_phone__contains=user_phone)
    result = result.filter(**kwargs).order_by('send_time')[start: end]
    return EmailSerializer(result, many=True).data


@filter_none_param
def get_email_total(**kwargs):
    result = Email.objects
    if kwargs.get('email_title'):
        email_title = kwargs.get('email_title')
        kwargs.pop('email_title')
        result = result.filter(email_title__contains=email_title)
    if kwargs.get('email_receiver'):
        email_receiver = kwargs.get('email_receiver')
        kwargs.pop('email_receiver')
        result = result.filter(email_receiver__contains=email_receiver)
    # if kwargs.get('user_name'):
    #     user_name = kwargs.get('user_name')
    #     kwargs.pop('user_name')
    #     result = result.filter(user_name__contains=user_name)
    # if kwargs.get('user_phone'):
    #     user_phone = kwargs.get('user_phone')
    #     kwargs.pop('user_phone')
    #     result = result.filter(user_phone__contains=user_phone)
    result = result.filter(**kwargs)
    return len(EmailSerializer(result, many=True).data)
