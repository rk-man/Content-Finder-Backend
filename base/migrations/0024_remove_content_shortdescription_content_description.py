# Generated by Django 4.1.2 on 2022-12-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_alter_content_coverimage_alter_profile_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='shortDescription',
        ),
        migrations.AddField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]