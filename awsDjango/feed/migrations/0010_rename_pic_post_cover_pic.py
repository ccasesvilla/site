# Generated by Django 3.2.7 on 2021-09-14 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20210914_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pic',
            new_name='cover_Pic',
        ),
    ]