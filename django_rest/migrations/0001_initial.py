# Generated by Django 3.2.7 on 2021-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meterReadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=100)),
                ('flat', models.IntegerField()),
                ('choicesMater', models.CharField(choices=[('GAS', 'Gas'), ('WATER', 'Water'), ('LIGHT', 'Light')], default='GAS', max_length=10)),
                ('metereRadings', models.IntegerField()),
            ],
        ),
    ]
