# Generated by Django 2.1.2 on 2018-11-12 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('website_core', '0005_auto_20181112_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplepage',
            name='background',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
