
from django.contrib import admin
from django.urls import path,include
from .views import home_view,how_view,about_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home_view,name="home"),
    path("about/",about_view,name="about"),
    path("how_it_works/",how_view,name="how_it_works"),
    path("testpsychotechnique/", include('testpsychotechnique.urls', namespace='testpsychotechnique')),
]
