# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core import get_excel_response


# Create your views here.
class ExcelView(APIView):

    def get(self, request):
        name = u'wangbobo'
        titles = ['title1', 'title2', 'title3']
        rows = [['row1', 'row2', 'row3']]
        column_widths = [10, 20, 30]
        response = get_excel_response(name, titles, rows, column_widths)
        return response
