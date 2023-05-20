from django.shortcuts import render

# library django-rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# library python
import json

# model
from .models import TDSMonitoring
# Create your views here.


class SaveDataTDS(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        uni = request.body.decode('utf-8')
        body = json.loads(uni)
        try:
            TDSMonitoring.objects.create(
                tds_value=body['tds'], temperature_value=body['temperature'],
                sensor=body['sensor'],
            )
            msg = "data berhasil disimpan"
        except Exception as e:
            msg = str(e)

        return Response({"msg": msg})
