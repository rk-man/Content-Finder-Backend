# Generated by Django 4.1.2 on 2022-12-03 05:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_profile_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(default='images/user-profiles/default-profile.png', upload_to='images/user-profiles/'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='images/cover-images')),
                ('shortDescription', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fileType', models.CharField(choices=[('photoshop', 'Adobe Photoshop'), ('adobe illustrator', 'Adobe Illustrator'), ('figma', 'Figma'), ('zip', 'Zip File'), ('after effects', 'Adobe After Effects'), ('others', 'Other files')], max_length=200)),
                ('contentType', models.CharField(choices=[('.png', 'Adobe Photoshop'), ('.ai', 'Adobe Illustrator'), ('.fig', 'Figma'), ('.aep', 'Adobe After Effects'), ('others', 'Other files')], max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
    ]
