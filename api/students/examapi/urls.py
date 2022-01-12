from django.urls import path
from .views import ExamList
from . import views

urlpatterns = [
        path('', ExamList.as_view()),
        path('<str:reg>/', views.exam_detail)
        ]
