from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Fee
        lookup_field = 'reg_number'



