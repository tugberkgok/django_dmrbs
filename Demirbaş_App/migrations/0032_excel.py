# Generated by Django 3.2.6 on 2021-09-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demirbaş_App', '0031_auto_20210827_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Dosya')),
            ],
        ),
    ]
