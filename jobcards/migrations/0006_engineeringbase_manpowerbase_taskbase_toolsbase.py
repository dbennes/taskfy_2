# Generated by Django 5.2.3 on 2025-06-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0005_alter_jobcard_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineeringBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('discipline', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=100)),
                ('rev', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManpowerBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('discipline', models.CharField(max_length=100)),
                ('working_code', models.CharField(max_length=20)),
                ('working_description', models.TextField()),
                ('direct_labor', models.CharField(max_length=100)),
                ('qty', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('discipline', models.CharField(max_length=100)),
                ('working_code', models.CharField(max_length=50)),
                ('typical_task', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ToolsBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('discipline', models.CharField(max_length=100)),
                ('working_code', models.CharField(max_length=50)),
                ('direct_labor', models.CharField(max_length=100)),
                ('qty_direct_labor', models.FloatField()),
                ('special_tooling', models.CharField(max_length=255)),
                ('qty', models.FloatField()),
            ],
        ),
    ]
