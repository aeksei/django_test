# Generated by Django 3.1.1 on 2020-10-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201013_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('1', 'fruct'), ('2', 'veg'), (None, 'Unknown')], max_length=20, null=True),
        ),
    ]
