from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    option = request.POST['operation']

    if option == "add":
        res = num1 + num2
    if option == "sub":
        res = num1 - num2
    if option == "mul":
        res = num1*num2
    return render(request, 'myapp/result.html', {'res': res})