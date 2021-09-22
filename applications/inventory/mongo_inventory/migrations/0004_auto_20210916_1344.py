# Generated by Django 3.2.6 on 2021-09-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongo_inventory', '0003_auto_20210912_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mongoconsumed',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mongoconsumed',
            name='mongo_id',
            field=models.CharField(default='19636432', editable=False, max_length=255, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mongoinventory',
            name='mongo_id',
            field=models.CharField(default='33038840', editable=False, max_length=255, verbose_name='ID'),
        ),
    ]