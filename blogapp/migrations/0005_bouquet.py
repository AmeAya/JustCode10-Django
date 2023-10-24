# Generated by Django 4.2.6 on 2023-10-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_flowertype_flower_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flowers', models.ManyToManyField(to='blogapp.flower')),
            ],
        ),
    ]
