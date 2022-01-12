from django.urls import path
from .views import FeeList
from . import views

urlpatterns = [
        path('', FeeList.as_view()),
        path('<str:reg>/', views.fee_detail)
        ]
