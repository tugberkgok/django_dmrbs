# Generated by Django 3.2.6 on 2021-09-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demirbaş_App', '0035_device_iz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='iz',
            field=models.CharField(blank=True, max_length=100000000, null=True, verbose_name='Eski Kullanıcı / Tarih'),
        ),
    ]
