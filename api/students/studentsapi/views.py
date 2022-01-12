from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#class StudentDetail(generics.RetrieveAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer

#    def get_queryset(self):
#        reg_number = self.request.query_params.get('reg')

#        queryset = Student.objects.filter(reg_number = reg_number)
#        return queryset

@api_view(['GET'])
def student_detail(request, reg):
    try:
        student = Student.objects.get(reg_number=reg)
    except:
        return JsonResponse('Error', safe=False)

    serializer = StudentSerializer(student, context={'request':request})
    return Response(serializer.data)


