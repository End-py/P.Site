# Generated by Django 3.2.7 on 2021-09-14 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210914_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image_5',
            new_name='image',
        ),
    ]