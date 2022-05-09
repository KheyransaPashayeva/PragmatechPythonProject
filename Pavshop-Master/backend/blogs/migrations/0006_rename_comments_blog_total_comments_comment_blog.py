# Generated by Django 4.0.3 on 2022-04-13 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_published_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='comments',
            new_name='total_comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blogs.blog'),
            preserve_default=False,
        ),
    ]
