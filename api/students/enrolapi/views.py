from django.shortcuts import render
from rest_framework import generics
from .models import Enrol
from .serializers import EnrolSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class EnrolList(generics.ListAPIView):
    queryset = Enrol.objects.all()
    serializer_class = EnrolSerializer

#class StudentDetail(generics.RetrieveAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer

#    def get_queryset(self):
#        reg_number = self.request.query_params.get('reg')

#        queryset = Student.objects.filter(reg_number = reg_number)
#        return queryset

@api_view(['GET'])
def enrol_detail(request, reg):
    try:
        enrol = Enrol.objects.get(reg_number=reg)
    except:
        return JsonResponse('Error', safe=False)

    serializer = EnrolSerializer(enrol, context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def enrolme(request,reg):
    try:
        myrequest = request.data
        status = myrequest.get('enrol_status')
        first_name = myrequest.get('first_name')
        second_name = myrequest.get('second_name')
        semester = myrequest.get('semester')
        reg_number = reg
        if status == 'True':
            status = True
        Enrol.objects.filter(reg_number=reg).update(enrol_status=status, first_name=first_name,
                second_name=second_name, semester=semester,
                reg_number=reg_number)
    except Exception as e:
        return JsonResponse('error ', e, safe=False)
    return JsonResponse('You have been registered', safe=False)


