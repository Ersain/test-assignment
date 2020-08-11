from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('disciplines/', views.discipline_list, name='discipline_list'),
    path('disciplines/<int:pk>', views.discipline_detail, name='discipline_detail')
]