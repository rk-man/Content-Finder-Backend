# Generated by Django 4.1.2 on 2022-12-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_profile_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='content_like', to='base.profile'),
        ),
    ]
