import folium

from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(request, folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        request.build_absolute_uri(image_url.url),
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = timezone.localtime()
    pokemon_entity = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time,
    )
    for pokemon in pokemon_entity:
        add_pokemon(
            request,
            folium_map,
            pokemon.lat,
            pokemon.lon,
            pokemon.pokemon.image
        )
    pokemons_on_page = Pokemon.objects.all()

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    next_evolutions = pokemon.next_evolutions.all()
    next_evolution = next_evolutions.first()
    requested_pokemon = {
        'title_ru': pokemon.title,
        'img_url': pokemon.image.url,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'previous_evolution': pokemon.previous_evolution,
        'next_evolution': next_evolution
    }

    current_time = timezone.localtime()
    pokemon_entities = pokemon.entities.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time,
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entities:
        add_pokemon(
            request,
            folium_map,
            pokemon.lat,
            pokemon.lon,
            pokemon.pokemon.image
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
