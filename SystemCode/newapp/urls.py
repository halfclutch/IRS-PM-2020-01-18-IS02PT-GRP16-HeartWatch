from django.urls import path
from . import views
app_name = 'newapp'

urlpatterns = [
    path('', views.questionnaire01, name='questionnaire01'),
    path('questionnaire01', views.questionnaire01, name='questionnaire01'),
    path('questionnaire02', views.questionnaire02, name='questionnaire02'),
    path('result', views.result, name='result'),
]

