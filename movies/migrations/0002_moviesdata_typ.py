# Generated by Django 5.1.1 on 2024-09-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='typ',
            field=models.CharField(default='action', max_length=300),
        ),
    ]
