# Generated by Django 3.1.14 on 2022-11-02 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0019_auto_20221102_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default='Покемон не указан', on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_essences', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
