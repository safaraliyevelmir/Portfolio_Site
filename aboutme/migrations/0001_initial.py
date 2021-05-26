# Generated by Django 3.2.3 on 2021-05-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(upload_to='')),
                ('CV', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Main_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Information', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Other_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=30)),
            ],
        ),
    ]
