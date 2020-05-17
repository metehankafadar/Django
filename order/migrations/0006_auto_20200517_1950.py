# Generated by Django 3.0.4 on 2020-05-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200517_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('New', 'New'), ('Accepted', 'Accepted'), ('Prepearing', 'Prepearing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('New', 'New'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
