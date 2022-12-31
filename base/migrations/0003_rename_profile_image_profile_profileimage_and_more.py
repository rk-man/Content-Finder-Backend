# Generated by Django 4.1.2 on 2022-10-28 04:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='profileImage',
        ),
        migrations.AddField(
            model_name='profile',
            name='createdAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='StockPhotoItem',
            fields=[
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='images/cover-images')),
                ('shortDescription', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoshopItem',
            fields=[
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='images/cover-images')),
                ('shortDescription', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
    ]