# Generated by Django 3.2.3 on 2021-05-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0005_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
