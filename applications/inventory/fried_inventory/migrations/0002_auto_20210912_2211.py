# Generated by Django 3.1.2 on 2021-09-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fried_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friedinventory',
            name='batch_no',
            field=models.CharField(max_length=255, verbose_name='FID'),
        ),
    ]