# Generated by Django 3.2.7 on 2021-09-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_alter_post_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
