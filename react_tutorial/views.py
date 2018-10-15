from django.shortcuts import render

# Create your views here.
def react_hello_world(request):
    return render(request, "hello_world.html", {})