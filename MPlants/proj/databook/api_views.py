from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import viewsets
from . import models
from . import serializers


@csrf_exempt
def Date_list(request):
    if request.method=='GET':
        dates=models.Date.objects.all()
        serializer = serializers.DateSerializer(dates, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        day = request.POST
        serializer = serializers.DateSerializer(data=day)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

class DateListAPIView(generics.ListAPIView):
    queryset = models.Date.objects.all()
    serializer_class = serializers.DateSerializer
class DateDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Date.objects.all()
    serializer_class = serializers.DateSerializer
class DateUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Date.objects.all()
    serializer_class = serializers.DateSerializer


class DateModelViewSet(viewsets.ModelViewSet):
    queryset = models.Date.objects.all()
    serializer_class = serializers.DateSerializer
