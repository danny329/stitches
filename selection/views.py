from django.shortcuts import render

# Create your views here.
def selectionpage(request):
    return render(request, 'selectionpage.html')