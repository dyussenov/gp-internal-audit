# Generated by Django 4.2 on 2023-06-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0008_alter_storage_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default=100),
        ),
    ]
