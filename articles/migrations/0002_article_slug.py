# Generated by Django 4.1.1 on 2022-09-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50), editable=False),
        ),
    ]
