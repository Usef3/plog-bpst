# Generated by Django 5.0.3 on 2024-04-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_post_delete_postpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bg_img',
            field=models.ImageField(upload_to='imges/%y/%m/%d/bg_img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(upload_to='imges/%y/%m/%d/post_img'),
        ),
    ]
