from django.shortcuts import render, HttpResponse

def todo_app(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("This is about page")

