# Generated by Django 2.0.9 on 2018-12-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0007_auto_20181203_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='End Time'),
        ),
        migrations.AddField(
            model_name='contest',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_date',
            field=models.DateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]