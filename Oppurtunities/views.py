from django.shortcuts import render

# Create your views here.
def avalible_oppurtunities(request):
    return render(request, 'Oppurtunities/avalabile_list.html', {})
