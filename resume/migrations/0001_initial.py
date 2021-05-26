# Generated by Django 3.2.3 on 2021-05-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('startdate', models.CharField(max_length=13)),
                ('enddate', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('per', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Working_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('startdate', models.CharField(max_length=13)),
                ('enddate', models.CharField(max_length=13)),
            ],
        ),
    ]
