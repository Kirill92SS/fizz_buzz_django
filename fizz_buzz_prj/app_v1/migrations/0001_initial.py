# Generated by Django 5.0.4 on 2024-04-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True)),
                ('data', models.CharField(default='FizzBuzz', max_length=10)),
            ],
        ),
    ]
