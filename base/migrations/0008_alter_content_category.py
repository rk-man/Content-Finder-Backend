# Generated by Django 4.1.2 on 2022-12-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_content_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(blank=True, choices=[('advertisement', 'Advertisement'), ('resume', 'Resume'), ('youtube', 'YouTube'), ('websites', 'Websites'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('others', 'Others')], max_length=200, null=True),
        ),
    ]
