# Generated by Django 3.2.6 on 2021-09-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrudate_inventory', '0003_auto_20210912_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrudateinventory',
            name='extru_id',
            field=models.CharField(default='45816936', editable=False, max_length=255, verbose_name='ID'),
        ),
    ]
