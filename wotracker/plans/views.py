from django.shortcuts import render
from rest_framework.views import APIView
from .models import PlansModel
from .serializers import PlansDetailSerializers
from rest_framework.response import Response
from rest_framework import status



class PlansDetailView(APIView):
    def get(self, request):
        plans = PlansModel.objects.all()
        serializer = PlansDetailSerializers(plans, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlansDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

