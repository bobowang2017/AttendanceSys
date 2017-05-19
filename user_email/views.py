# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.process import response_data
from user_email.core import send_email, get_email, get_email_total


class EmailView(APIView):

    def get(self, request):
        page_num = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('rows', 10))
        email_receiver = request.query_params.get('email_receiver', None)
        email_receiver = None if str(email_receiver) == '' else email_receiver
        email_title = request.query_params.get('email_title', None)
        email_title = None if str(email_title) == '' else email_title
        try:
            email_list = get_email(page_num, page_size, email_title=email_title, email_receiver=email_receiver)
            email_total = get_email_total(email_title=email_title, email_receiver=email_receiver)
            data = dict()
            data['rows'] = email_list
            data['total'] = email_total
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', e), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', data), status=status.HTTP_200_OK)

    def post(self, request):
        try:
            receiver_list = request.data.get('receiver_list')
            header = request.data.get('header')
            content = request.data.get('content')
            if receiver_list is None or header is None or content is None:
                return Response(response_data(-1, 'error', 'Param Email is None'), status=status.HTTP_200_OK)
            result = send_email(str(receiver_list), str(header), str(content))
            if result == 0:
                raise Exception(u'邮件发送异常')
        except Exception as e:
            traceback.print_exc()
            return Response(response_data(-2, 'exception', str(e)), status=status.HTTP_200_OK)
        return Response(response_data(0, 'success', None), status=status.HTTP_200_OK)