# Generated by Django 4.0.3 on 2022-04-12 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comment_rename_tittle_blog_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]