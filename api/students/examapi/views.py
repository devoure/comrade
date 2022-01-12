from django.shortcuts import render
from rest_framework import generics
from .models import Exam
from .serializers import ExamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class ExamList(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

#class StudentDetail(generics.RetrieveAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer

#    def get_queryset(self):
#        reg_number = self.request.query_params.get('reg')

#        queryset = Student.objects.filter(reg_number = reg_number)
#        return queryset

@api_view(['GET'])
def exam_detail(request, reg):
    try:
        exam = Exam.objects.filter(reg_number=reg)
    except:
        return JsonResponse('Error', safe=False)

    serializer = ExamSerializer(exam, context={'request':request}, many=True)
    return Response(serializer.data)


