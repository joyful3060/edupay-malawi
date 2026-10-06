from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('add-payment/', views.add_payment, name='add_payment'),
]