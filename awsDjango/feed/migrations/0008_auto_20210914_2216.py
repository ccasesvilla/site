# Generated by Django 3.2.7 on 2021-09-14 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.AddField(
            model_name='post',
            name='Cover Photo',
            field=models.FileField(blank=True, default='default.jpg', upload_to='path/to/img'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='feed.post'),
        ),
    ]