# Generated by Django 4.2.2 on 2023-12-22 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStripe',
            fields=[
                ('price_id', models.CharField(max_length=35)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.item')),
            ],
        ),
    ]