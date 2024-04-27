# Generated by Django 5.0.4 on 2024-04-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buzz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True)),
                ('data', models.CharField(default='Buzz', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True)),
                ('data', models.CharField(default='Fizz', max_length=10)),
            ],
        ),
    ]