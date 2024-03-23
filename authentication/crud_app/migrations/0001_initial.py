# Generated by Django 5.0.3 on 2024-03-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=10)),
                ('product_price', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(choices=[('Online', 'ONLINE'), ('Cash', 'Cash On Delivery')], max_length=10)),
            ],
        ),
    ]
