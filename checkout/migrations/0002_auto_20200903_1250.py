# Generated by Django 3.0.8 on 2020-09-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_instructions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(default='+44 7700 900796', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]