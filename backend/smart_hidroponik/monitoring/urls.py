from django.urls import re_path, include
from .views import SaveDataTDS

urlpatterns = [
    re_path(r'^tds_save/$', SaveDataTDS.as_view(), name='fetch_data'),
]
