# Generated by Django 3.2.7 on 2021-09-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_rename_pic_post_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_Pic',
            field=models.FileField(blank=True, default=None, upload_to='path/to/img'),
        ),
    ]
