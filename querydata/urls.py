from django.urls import path
from . import views

app_name = 'querydata'
urlpatterns = [
    path('process_country_code/', views.process_country_code, name='process_country_code'),
]
