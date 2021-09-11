# Generated by Django 3.1.2 on 2021-09-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtruDateInventory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_settings.basemodel')),
                ('extru_id', models.CharField(default='25290176', editable=False, max_length=255, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=255, verbose_name='Batch No.')),
                ('date_produced', models.DateField(verbose_name='Date Produced')),
                ('total_volume', models.IntegerField(verbose_name='Total Volume (kg.)')),
                ('mongo_batch_no', models.CharField(max_length=255, verbose_name='Batch No. of Mongo')),
                ('rice_batch_no', models.CharField(max_length=255, verbose_name='Batch No. of Rice')),
                ('sesame_batch_no', models.CharField(max_length=255, verbose_name='Batch No. of Sesame')),
            ],
            options={
                'verbose_name': 'ExtruDates',
                'verbose_name_plural': 'ExtruDates',
            },
            bases=('base_settings.basemodel',),
        ),
    ]
