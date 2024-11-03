from django.shortcuts import render

def index(request):
    # Render the welcome.html template
    return render(request, 'welcome.html')

