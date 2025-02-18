from django.shortcuts import render
from rest_framework.views import APIView
from .models import PlansModel
from .serializers import PlansDetailSerializers
from rest_framework.response import Response



class PlansDetailView(APIView):
    def get(self, request):
        plans = PlansModel.objects.all()
        serializer = PlansDetailSerializers(plans, many=True)
        return Response(serializer.data)

