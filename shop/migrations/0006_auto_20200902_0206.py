# Generated by Django 3.1 on 2020-09-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_productimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='name',
            field=models.CharField(db_index=True, default='1', max_length=200),
        ),
    ]
