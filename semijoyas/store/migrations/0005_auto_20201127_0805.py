# Generated by Django 3.1.1 on 2020-11-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('Ar', 'Aros'), ('An', 'Anillos'), ('C', 'Collares'), ('Pi', 'Piercing Fake'), ('Pu', 'Pulseras'), ('To', 'Tobilleras')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
