# Generated by Django 5.2.3 on 2025-06-27 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0015_jobcardnew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobcardnew',
            old_name='item',
            new_name='items',
        ),
    ]
