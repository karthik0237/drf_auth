# Generated by Django 5.0.3 on 2024-04-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('category', models.CharField(default='All', max_length=32)),
                ('mfg_date', models.DateField(default=None)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
