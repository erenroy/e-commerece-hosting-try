# Generated by Django 4.2.3 on 2023-08-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='blogpic'),
        ),
    ]