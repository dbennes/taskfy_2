# Generated by Django 5.2.3 on 2025-06-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0003_alter_jobcard_hot_work_required_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcard',
            name='approved_br',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobcard',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobcard',
            name='rev',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
