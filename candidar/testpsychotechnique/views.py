from django.shortcuts import render

# Create your views here.
def qcm_view(request):
    return render(request,'testpsychotechnique/index.html')

def interviewers_view(request):
    return render(request,'testpsychotechnique/interviwers.html')

def formulaire_view(request):
    return render(request,"testpsychotechnique/formulaire.html")