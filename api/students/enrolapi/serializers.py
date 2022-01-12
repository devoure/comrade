from rest_framework import serializers
from .models import Enrol

class EnrolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Enrol
        lookup_field = 'reg_number'



