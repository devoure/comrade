from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Exam
        lookup_field = 'reg_number'



