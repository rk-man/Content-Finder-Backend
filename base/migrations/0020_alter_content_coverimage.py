# Generated by Django 4.1.2 on 2022-12-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_profile_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='coverImage',
            field=models.ImageField(blank=True, null=True, upload_to='cover-images/'),
        ),
    ]
