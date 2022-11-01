from django.db import models  # noqa F401


class Pokemon(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(blank=True)
    title_en = models.CharField(max_length=50, blank=True)
    title_jp = models.CharField(max_length=50, blank=True)
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default='', blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strenght = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon.title}. Координаты: {self.lat}; {self.lon}'