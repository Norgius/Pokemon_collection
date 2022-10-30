from django.db import models  # noqa F401


class Pokemon(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):

    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.lat}; {self.lon}'