# Generated by Django 4.1.2 on 2022-12-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_content_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contentType',
            field=models.CharField(choices=[('Adobe Photoshop ', '.psd (photoshop)'), ('Adobe Illustrator ', '.ai (illustrator)'), ('Figma ', '.fig (figma)'), ('Adobe After Effects ', '.aep (after effects)'), ('Other files ', 'others')], max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='fileType',
            field=models.CharField(choices=[('photoshop', '.psd (photoshop)'), ('adobe illustrator', '.ai (illustrator)'), ('figma', '.fig (figma)'), ('zip', '.zip (zip file)'), ('after effects', '.aep (after effects)'), ('others', 'others')], max_length=200),
        ),
    ]
