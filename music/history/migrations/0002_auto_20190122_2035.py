# Generated by Django 2.1.5 on 2019-01-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
