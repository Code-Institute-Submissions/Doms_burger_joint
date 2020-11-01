# Generated by Django 3.0.8 on 2020-11-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20201027_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity_count',
        ),
        migrations.AddField(
            model_name='order',
            name='item_quantity_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='combo_quantity_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
