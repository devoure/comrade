from django.urls import path
from .views import StudentList
from . import views

urlpatterns = [
        path('', StudentList.as_view()),
        path('<str:reg>/', views.student_detail)
        ]
