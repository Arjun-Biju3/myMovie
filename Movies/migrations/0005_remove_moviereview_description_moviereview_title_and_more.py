# Generated by Django 5.0.6 on 2024-07-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0004_alter_moviecomments_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviereview',
            name='description',
        ),
        migrations.AddField(
            model_name='moviereview',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='review',
            field=models.CharField(max_length=250),
        ),
    ]
