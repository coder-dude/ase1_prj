# Generated by Django 2.1.2 on 2018-12-14 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20181214_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submitted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]