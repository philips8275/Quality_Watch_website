# Generated by Django 5.2 on 2025-06-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_products_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='style',
            field=models.CharField(choices=[('Professional', 'Professional'), ('Trendy', 'Trendy'), ('Luxury', 'Luxury'), ('Elegant', 'Elegant'), ('kids', 'Kids'), ('sports', 'sports'), ('smart', 'smart')], default='Elegant', max_length=50),
        ),
    ]
