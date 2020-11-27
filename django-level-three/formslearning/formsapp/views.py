from django.shortcuts import render
from formsapp import forms
# Create your views here.
def index(request):
    return render(request,'formsapp/index.html')


def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request,'formsapp/forms.html',{'form':form})
