# Generated by Django 3.2.7 on 2021-09-22 14:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210921_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='post', unique_with=('created_on',)),
        ),
    ]
