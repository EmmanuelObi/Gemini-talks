# Generated by Django 3.0.7 on 2020-07-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gemini', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
