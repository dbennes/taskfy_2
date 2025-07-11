# Generated by Django 5.2.3 on 2025-06-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0006_engineeringbase_manpowerbase_taskbase_toolsbase'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.PositiveIntegerField()),
                ('discipline', models.CharField(max_length=100)),
                ('working_code', models.CharField(max_length=50)),
                ('pmto_code', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('qty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Material Base',
                'verbose_name_plural': 'Materials Base',
            },
        ),
    ]
