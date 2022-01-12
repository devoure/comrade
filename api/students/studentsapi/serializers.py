from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('gender', 'first_name', 'second_name', 'reg_number',
                'course', 'secret_key','current_year', 'current_semester',
                'date_joined')
        model = Student
        lookup_field = 'reg_number'



