from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Person

# Create your views here.

def index(request):
    #pList = Person.objects.get()
    pList = get_list_or_404(Person)
    return render(request, 'person_index.html', {'pList': pList})
    

def details(request, pid='0'):
        p = get_object_or_404(Person, pk=pid)
        return render(request, 'person_details.html', {'p':p})
