# -*- coding: utf-8 -*-
from rest_framework import serializers
from user_email.models import Email
from django.conf.global_settings import DATETIME_INPUT_FORMATS


class EmailSerializer(serializers.ModelSerializer):
    EMAIL_STATUS = (
        (0, '未读'),
        (1, '已读'),
        (-1, '删除')
    )

    email_id = serializers.CharField(max_length=64)
    email_sender = serializers.CharField(allow_blank=False, max_length=64)
    email_receiver = serializers.CharField(allow_blank=False, max_length=64)
    email_title = serializers.CharField(allow_blank=False, max_length=256)
    email_content = serializers.CharField(allow_blank=False,)
    send_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
                                          input_formats=DATETIME_INPUT_FORMATS, required=False)
    email_status = serializers.ChoiceField(choices=EMAIL_STATUS, default=0)

    class Meta:
        model = Email
        fields = serializers.ALL_FIELDS

    def create(self, validated_data):
        return Email.objects.create(**validated_data)

    def update(self, email, validated_data):
        email.email_id = validated_data.get('email_id', email.email_id)
        email.email_sender = validated_data.get('email_sender', email.email_sender)
        email.email_receiver = validated_data.get('email_receiver', email.email_receiver)
        email.email_title = validated_data.get('email_title', email.email_title)
        email.email_content = validated_data.get('email_content', email.email_content)
        email.send_time = validated_data.get('send_time', email.send_time)
        email.email_status = validated_data.get('email_status', email.email_status)
        email.save()
        return email
