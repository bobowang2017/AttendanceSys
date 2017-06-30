from django.conf.urls import url
from views import ExcelView

urlpatterns = [
    url(r'^excel$', ExcelView.as_view()),
]
