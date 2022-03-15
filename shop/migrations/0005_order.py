# Generated by Django 4.0.2 on 2022-03-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_complain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=3000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
            ],
        ),
    ]