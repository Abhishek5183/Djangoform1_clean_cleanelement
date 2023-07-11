from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse

# Create your views here.
def djangoform(request):
    s_form = Registration()
    d = {'s_form' : s_form}
    if request.method == 'POST':
        s_data = Registration(request.POST)
        if s_data.is_valid():
            return HttpResponse(str(s_data.cleaned_data))
        else:
            return HttpResponse('Please enter valid data')
    return render(request, 'djangoform.html', d)

