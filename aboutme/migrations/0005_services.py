# Generated by Django 3.2.3 on 2021-05-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0004_auto_20210519_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=300)),
            ],
        ),
    ]
