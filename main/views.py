from django.forms import model_to_dict
from django.shortcuts import render
from .models import Travel, Carrier, Hotel
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TravelSerializer

# Create your views here.


class TravelAPIView(APIView):

    def get(self, request: Request) -> Response:
        newses = Travel.objects.all()
        return Response({"newses": TravelSerializer(newses, many=True).data})
    

    def post(self, request: Request):

        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        news = serializer.save()

        return Response({'news': TravelSerializer(news).data, 'message': "Maqola qo'shildi!!!"})

    def put(self, request: Request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        try:
            news = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(news, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_news = serializer.save()
            return Response({'news': TravelSerializer(updated_news).data})
        except:
            return Response({'error': "Bu id da maqola mavjud emas"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            news = Travel.objects.get(pk=pk)
            news.delete()
            return Response({'success': "Maqola o'chirildi"})
        except:
            return Response({'error': "Bu id da maqola mavjud emas"})

