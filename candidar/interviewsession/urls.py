
from django.urls import path,include
from .views import interview_view
app_name = 'interviewsession' 
urlpatterns = [
    path("",interview_view,name="index"),
    path("graduation/",include("graduation.urls",namespace="graduation")),
]