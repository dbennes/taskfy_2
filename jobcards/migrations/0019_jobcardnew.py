# Generated by Django 5.2.3 on 2025-06-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0018_delete_jobcardnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCardNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('seq_number', models.CharField(max_length=10)),
                ('discipline', models.CharField(max_length=50)),
                ('discipline_code', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=10)),
                ('activity_id', models.CharField(max_length=50)),
                ('start', models.DateField(blank=True, null=True)),
                ('finish', models.DateField(blank=True, null=True)),
                ('system', models.CharField(max_length=20)),
                ('subsystem', models.CharField(max_length=20)),
                ('workpack_number', models.CharField(max_length=20)),
                ('working_code', models.CharField(max_length=20)),
                ('tag', models.CharField(max_length=50)),
                ('working_code_description', models.TextField()),
                ('job_card_number', models.CharField(max_length=50)),
                ('rev', models.CharField(blank=True, max_length=10, null=True)),
                ('jobcard_status', models.CharField(max_length=50)),
                ('job_card_description', models.TextField()),
                ('completed', models.CharField(max_length=10)),
                ('total_weight', models.CharField(max_length=30)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('total_duration_hs', models.CharField(blank=True, max_length=30, null=True)),
                ('indice_kpi', models.CharField(blank=True, max_length=30, null=True)),
                ('total_man_hours', models.CharField(blank=True, max_length=30, null=True)),
                ('prepared_by', models.CharField(max_length=100)),
                ('date_prepared', models.DateField(blank=True, null=True)),
                ('approved_br', models.CharField(blank=True, max_length=50, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('hot_work_required', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
