from django.shortcuts import render

# Create your views here.
def graduation_view(request):
    return render(request,"graduation/index.html")