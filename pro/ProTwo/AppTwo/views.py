from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App<em>")

def help(request):
    my_dict = {'help_page':"HELP"}
    return render(request,'AppTwo/index.html',context=my_dict)

def users(request):
    usuarios = User.objects.order_by('us_fname')
    name_dict = {'users': usuarios}
    return render(request,'AppTwo/users.html', context=name_dict)
