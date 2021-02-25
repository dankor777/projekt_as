# Generated by Django 3.0.6 on 2021-01-11 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt_as', '0004_remove_komentarz_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentarz',
            name='post',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projekt_as.Post'),
            preserve_default=False,
        ),
    ]