# Generated by Django 3.1.7 on 2021-09-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SesameInventory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_settings.basemodel')),
                ('sesame_id', models.CharField(default='49289202', editable=False, max_length=255, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=255, verbose_name='Batch No.')),
                ('date_received', models.DateField(verbose_name='Date Received')),
                ('total_avail_volume', models.IntegerField(verbose_name='Total Available Volume')),
            ],
            options={
                'verbose_name': 'Sesame Inventory',
                'verbose_name_plural': 'Sesame Inventories',
                'db_table': 'sesame_inventory',
            },
            bases=('base_settings.basemodel',),
        ),
        migrations.CreateModel(
            name='SesameConsumed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sesame_id', models.CharField(default='29254438', editable=False, max_length=255, verbose_name='ID')),
                ('total_avail_volume', models.IntegerField(verbose_name='Total Available Volume')),
                ('amount_consumed', models.IntegerField(blank=True, null=True, verbose_name='Amount Consumed')),
                ('date_consumed', models.DateField(blank=True, null=True, verbose_name='Date Consumed')),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesame_inventory', to='sesame_inventory.sesameinventory')),
            ],
            options={
                'verbose_name': 'Sesame Consumed',
                'verbose_name_plural': 'Sesame Consumed',
                'db_table': 'sesame_consumed',
            },
        ),
    ]
