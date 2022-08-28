from django.shortcuts import render

def hello(request):
    name = request.GET['name']
    message = request.GET['message']
    return render(request, 'hello.html', {'name': name, 'message': message})

