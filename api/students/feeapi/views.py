from django.shortcuts import render
from rest_framework import generics
from .models import Fee
from .serializers import FeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class FeeList(generics.ListAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

#class StudentDetail(generics.RetrieveAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer

#    def get_queryset(self):
#        reg_number = self.request.query_params.get('reg')

#        queryset = Student.objects.filter(reg_number = reg_number)
#        return queryset

@api_view(['GET'])
def fee_detail(request, reg):
    try:
        fee = Fee.objects.get(reg_number=reg)
    except:
        return JsonResponse('Error', safe=False)

    serializer = FeeSerializer(fee, context={'request':request})
    return Response(serializer.data)


