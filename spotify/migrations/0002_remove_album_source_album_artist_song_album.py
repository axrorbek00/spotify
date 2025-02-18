# Generated by Django 4.2.11 on 2024-03-14 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='source',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='spotify.artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spotify.album'),
        ),
    ]
