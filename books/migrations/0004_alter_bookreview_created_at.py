# Generated by Django 5.0.1 on 2024-01-11 15:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_bookreview_created_at_alter_bookreview_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
