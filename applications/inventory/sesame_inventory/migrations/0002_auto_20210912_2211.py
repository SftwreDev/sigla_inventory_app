# Generated by Django 3.1.2 on 2021-09-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesame_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesameconsumed',
            name='sesame_id',
            field=models.CharField(default='24465593', editable=False, max_length=255, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sesameinventory',
            name='batch_no',
            field=models.CharField(max_length=255, verbose_name='SID'),
        ),
        migrations.AlterField(
            model_name='sesameinventory',
            name='sesame_id',
            field=models.CharField(default='11529822', editable=False, max_length=255, verbose_name='ID'),
        ),
    ]