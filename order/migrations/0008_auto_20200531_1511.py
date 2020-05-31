# Generated by Django 3.0.4 on 2020-05-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200531_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('New', 'New'), ('Prepearing', 'Prepearing'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('OnShipping', 'OnShipping')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
    ]