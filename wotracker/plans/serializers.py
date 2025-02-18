from rest_framework.serializers import ModelSerializer
from .models import PlansModel


class PlansDetailSerializers(ModelSerializer):
    class Meta:
        model = PlansModel
        fields = '__all__'