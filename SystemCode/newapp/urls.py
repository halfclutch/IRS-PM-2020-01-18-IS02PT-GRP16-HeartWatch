from django.urls import path
from . import views
app_name = 'newapp'

urlpatterns = [
    #path('', views.questionnaire01, name='questionnaire01'),
    path('', views.questionThal, name='questionThal'),
    #path('questionnaire01', views.questionnaire01, name='questionnaire01'),
    path('questionThal', views.questionThal, name='questionThal'),
    path('questionCP', views.questionCP, name='questionCP'),
    path('questionMaxhr', views.questionMaxhr, name='questionMaxhr'),
    path('questionFLVessels2', views.questionFLVessels2, name='questionFLVessels2'),
    path('questionFLVessels', views.questionFLVessels, name='questionFLVessels'),
    path('questionExang', views.questionExang, name='questionExang'),
    path('questionRestecg', views.questionRestecg, name='questionRestecg'),
    path('questionnaire02', views.questionnaire02, name='questionnaire02'),
    path('questionnaire03', views.questionnaire03, name='questionnaire03'),
    path('result', views.result, name='result'),
]

