from django.shortcuts import render


def home_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def how_view(request):
    return render(request,'how_work.html')
