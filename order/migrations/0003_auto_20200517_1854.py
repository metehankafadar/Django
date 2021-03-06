# Generated by Django 3.0.4 on 2020-05-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled'), ('New', 'New'), ('OnShipping', 'OnShipping'), ('Prepearing', 'Prepearing')], default='New', max_length=10),
        ),
    ]
