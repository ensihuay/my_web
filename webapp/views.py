from django.shortcuts import render

# Home
def home(request):
    context = {}
    return render(request, 'webapp/home.html', context)

def resumn_yu(request):
    context = {}
    return render(request, 'webapp/resumn/resumn_yu.html', context)