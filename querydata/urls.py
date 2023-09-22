from django.urls import path
from . import views
app_name = 'querydata'
urlpatterns = [
    path('get_country_banks/', views.country_code_input, name='country_code_input'),
    path('result/', views.result_view, name='result_view'),
]



# from django.urls import path
# from . import views

# app_name = 'querydata'
# urlpatterns = [
#     path('process_country_code/', views.process_country_code, name='process_country_code'),
# ]
