from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home1(request):
    return HttpResponse("OK")

def home(request):
    context={'student_list':
                [{
                    'name':'Ram',
                    'address':'Kathmandu',
                    'contact':'9847620206'
                },
                {
                    'name':'Shyam',
                    'address':'Bhaktapur',
                    'contact':'9880715922'
                },{
                    'name':'Sita',
                    'address':'Lalitpur',
                    'contact':'9844375899'
                }]
            }
    return render(request, 'home.html', context)