# Generated by Django 3.2.19 on 2023-06-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_image_filter_post_post_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../gro_default_post_lv2kj4', upload_to='images/'),
        ),
    ]
