from django.http import HttpResponse
from django.shortcuts import render

def studentlist(request):
    return render(request, 'studentlist.html')