# Generated by Django 4.2 on 2023-05-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0004_item_is_monthly_amortizations'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/items/'),
        ),
    ]
