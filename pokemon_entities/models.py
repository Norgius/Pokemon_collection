from django.db import models


class Pokemon(models.Model):

    title = models.CharField('Имя покемона', max_length=200)
    image = models.ImageField(
        'Изображение покемона',
        upload_to='images/',
        null=True,
    )
    description = models.TextField('Описание', blank=True)
    title_en = models.CharField('Имя на англ', max_length=50, blank=True)
    title_jp = models.CharField('Имя на японском', max_length=50, blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционировал',
        on_delete=models.CASCADE,
        related_name='next_evolutions',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        default='Покемон не указан',
        related_name='entities'
    )
    lat = models.FloatField('Широта', null=True)
    lon = models.FloatField('Долгота', null=True)
    appeared_at = models.DateTimeField('Появился', null=True)
    disappeared_at = models.DateTimeField('Исчез', null=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strenght = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon.title}. Координаты: {self.lat}; {self.lon}'
