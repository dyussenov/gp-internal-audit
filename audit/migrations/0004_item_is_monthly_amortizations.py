# Generated by Django 4.2 on 2023-05-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0003_storage_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_monthly_amortizations',
            field=models.BooleanField(default=False),
        ),
    ]
