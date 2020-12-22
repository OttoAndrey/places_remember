import folium
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PlaceForm
from .models import Place

KRSK_CENTER = [56.014899, 92.859867]


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    places = Place.objects.filter(user=request.user)

    if not places:
        places = False
        return render(request, 'home.html', context={'palces': places})

    geo = []
    for place in places:
        point = {
            'id': place.id,
            'title': place.title,
            'text': place.text,
        }
        geo.append(point)
    return render(request, 'home.html', context={'places': geo})


@login_required
def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            lat = form.cleaned_data['lat']
            lng = form.cleaned_data['lng']
            Place.objects.create(
                title=title,
                text=text,
                lat=lat,
                lng=lng,
                user=request.user,
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        folium_map = folium.Map(location=KRSK_CENTER, zoom_start=12)
        folium_map.add_child(folium.LatLngPopup())
        form = PlaceForm()
    return render(request, 'create_place.html', context={'form': form, 'map': folium_map._repr_html_()})


@login_required
def place_detail(request, place_id):
    place = Place.objects.filter(user=request.user, pk=place_id)[0]
    center = [place.lat, place.lng]
    folium_map = folium.Map(location=center, zoom_start=12)
    folium.Marker(center).add_to(folium_map)

    return render(request, 'place_detail.html', context={'place': place, 'map': folium_map._repr_html_()})
