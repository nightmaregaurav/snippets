# Generated by Django 3.2.4 on 2021-08-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20, unique=True)),
                ('value_string', models.CharField(blank=True, max_length=1000, null=True)),
                ('value_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
