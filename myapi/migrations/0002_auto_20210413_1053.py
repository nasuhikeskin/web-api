# Generated by Django 3.2 on 2021-04-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='agirlik',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='genislik',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='uzunluk',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='yukseklik',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
