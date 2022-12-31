# Generated by Django 4.1.2 on 2022-12-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_content_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contentType',
            field=models.CharField(choices=[('Adobe Photoshop ', '.png'), ('Adobe Illustrator ', '.ai'), ('Figma ', '.fig'), ('Adobe After Effects ', '.aep'), ('Other files ', 'others')], max_length=200),
        ),
    ]