from django.shortcuts import render

def home(request):
    values = {}
    return render(request, 'main/homepage.html', values)
