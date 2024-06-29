# Generated by Django 5.0.6 on 2024-06-27 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriescomments',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series_name1', to='series.series'),
        ),
        migrations.AlterField(
            model_name='seriesreview',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series_name2', to='series.series'),
        ),
    ]