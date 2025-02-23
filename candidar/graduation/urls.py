
from django.urls import path
from .views import graduation_view
app_name = 'graduation' 
urlpatterns = [
    path("",graduation_view,name="index"),
]
