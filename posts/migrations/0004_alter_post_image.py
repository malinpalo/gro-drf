# Generated by Django 3.2.19 on 2023-06-26 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../gro_default_post_t9nbw3', upload_to='images/'),
        ),
    ]
