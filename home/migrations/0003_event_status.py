# Generated by Django 4.1.4 on 2022-12-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]