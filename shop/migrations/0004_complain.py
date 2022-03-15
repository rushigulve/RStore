# Generated by Django 4.0.2 on 2022-03-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category_product_image_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('complain_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]