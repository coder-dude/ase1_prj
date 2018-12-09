# Generated by Django 2.0.9 on 2018-12-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20181202_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end_date',
            field=models.DateTimeField(verbose_name='End Date Time'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='is_public',
            field=models.BooleanField(default=True, help_text='If you choose to make this non public, please enter a link below that participants will                                  click to register for the contest. It can lead to a form or a website etc. After they complete                                   registration, it is your responsibility to add them in the participants list via                                   the REST API call.', verbose_name='Is this Public?'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start Date Time'),
        ),
    ]