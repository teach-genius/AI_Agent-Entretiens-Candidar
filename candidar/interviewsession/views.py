from django.shortcuts import render

# Create your views here.
def interview_view(request):
    return render(request,'interviewsession/index.html')