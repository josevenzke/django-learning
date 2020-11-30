from django.shortcuts import render
from userslist.models import User
# Create your views here.
def index(request):
    return render(request,'userslist/index.html')

def users(request):
    usuarios = User.objects.order_by('first_name')
    name_dict = {'users': usuarios}
    return render(request,'userslist/users.html',context=name_dict)
