from django.urls import path
from .views import EnrolList
from . import views

urlpatterns = [
        path('', EnrolList.as_view()),
        path('<str:reg>/', views.enrol_detail),
        path('enrolme/<str:reg>/', views.enrolme)
        ]
