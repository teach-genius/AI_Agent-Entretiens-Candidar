
from django.urls import path,include
from .views import formulaire_view,interviewers_view,qcm_view
app_name = 'testpsychotechnique' 
urlpatterns = [
    path("",formulaire_view,name="formulaire"),
    path("interviewers/",interviewers_view,name="interviewers"),
    path("qcm/",qcm_view,name="qcm"),
    path("interviewsession/",include("interviewsession.urls",namespace="interviewsession"))
]
