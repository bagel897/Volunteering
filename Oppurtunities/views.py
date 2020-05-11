from django.shortcuts import render
from django.utils import timezone
from .models import Oppurtunity


# Create your views here.
def avalible_oppurtunities(request):
    Oppurtunities = Oppurtunity.objects.all()
    return render(request, 'Oppurtunities/avalabile_list.html', {'Oppurtunities': Oppurtunities})
