import folium
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import PlaceForm
from .models import Place
from .utils import LatLngPopup

KRSK_CENTER = [56.014899, 92.859867]


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    places = request.user.places.order_by('-pk')

    if not places:
        return render(request, 'home.html', context={'places': places})

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
            Place.objects.create(**form.cleaned_data, user=request.user,)
            return HttpResponseRedirect(reverse('home'))
    else:
        folium_map = folium.Map(location=KRSK_CENTER, zoom_start=12)
        folium_map.add_child(LatLngPopup())
        form = PlaceForm()
    return render(request, 'create_place.html', context={'form': form, 'map': folium_map._repr_html_()})


@login_required
def place_detail(request, place_id):
    place = get_object_or_404(Place, user=request.user, pk=place_id)
    center = [place.lat, place.lng]
    folium_map = folium.Map(location=center, zoom_start=12)
    folium.Marker(center).add_to(folium_map)
    return render(request, 'place_detail.html', context={'place': place, 'map': folium_map._repr_html_()})
