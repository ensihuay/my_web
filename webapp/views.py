from django.shortcuts import render

# Home
def home(request):
    context = {}
    return render(request, 'webapp/home.html', context)
