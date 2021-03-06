# Generated by Django 4.0.3 on 2022-04-09 18:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the series name', max_length=512)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['series', '-series_volume_number']},
        ),
        migrations.AddField(
            model_name='book',
            name='series_volume_number',
            field=models.IntegerField(blank=True, help_text='Enter the number in the series this book falls- or leave blank', null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier of the book across all locations', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, help_text='Enter the series this book belongs to- or leave blank', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.series'),
        ),
    ]
