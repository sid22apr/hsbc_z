from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import json

# Create your views here.
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class GetFirstAPI(APIView):

    def get(self, request, *args, **kwargs):
        response = {}
        response['status'] = 500
        try:
            response['status'] = 200
        except Exception as e:
            e_type, e_object, e_tb = sys.exc_info()
        return Response(data=response)


class GetRecommendationAPI(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        response['status'] = 500
        try:
            data = request.data
            age = data['age']
            risk = data['risk']
            capital=data['capital']
            maturity=data['maturity']

            response['status'] = 200
            response['data']=age+risk+capital+maturity

        except Exception as e:
            e_type, e_object, e_tb = sys.exc_info()
        return Response(data=response)



GetFirst=GetFirstAPI.as_view()
GetRecommendation=GetRecommendationAPI.as_view()