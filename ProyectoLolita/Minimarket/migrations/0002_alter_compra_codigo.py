# Generated by Django 4.1.2 on 2022-11-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minimarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='codigo',
            field=models.TextField(max_length=50),
        ),
    ]
