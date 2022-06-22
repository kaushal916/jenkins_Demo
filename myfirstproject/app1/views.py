from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    "shows home page to the user"
    context = {'name':'Hanish'}
    return render(request, "app1/index.html", context)


def home2(request):
    "shows home page to the user"
    return HttpResponse("<html><body><h>Home Page2</h></body></html>")    

