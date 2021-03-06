# Generated by Django 2.1.2 on 2018-12-12 16:04

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import questions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=questions.models.image_upload_url)),
                ('back_image', models.ImageField(blank=True, null=True, upload_to=questions.models.back_image_upload_url)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=True, help_text='Keep questions inactive until their contests start!', verbose_name='Is Active?')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('short_description', models.TextField(help_text='A short description whch describes your question. This will be visible when                                          user hovers on your question the all questions page', max_length=250, verbose_name='Short Description')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description')),
                ('input_format', models.TextField(null='True', verbose_name='Input format')),
                ('constraints', models.TextField(null='True', verbose_name='Constraints')),
                ('output_format', models.TextField(null='True', verbose_name='Output format')),
                ('sample_input', models.TextField(null='True', verbose_name='Sample input')),
                ('sample_output', models.TextField(null='True', verbose_name='Sample output')),
                ('difficulty', models.CharField(choices=[(None, 'Choose Difficulty Level'), ('Unknown', 'Unknown'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=15, verbose_name='Difficulty level')),
                ('time_limit', models.FloatField(default=2.0, help_text='This is approx the time limit that will be required to run a python code                                       for the problem. This limit will be automatically reduced for other languages                                       like C which take much lesser time for similar implementation', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10, 'We currently do not allow any                                    code that runs for more than 10 secs')], verbose_name='Time Limit')),
                ('unique_code', models.CharField(db_index=True, help_text="A unique code for your question. between 3-15 characters. May contain only                                    lowercase characters and numbers. For example if the question name is 'Sorting Array',                                    you may name the code SORTARR", max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[0-9a-z]*$', 'The Unique code can contain only small case alphabets and numbers ')], verbose_name='Unique Code')),
                ('view_count', models.IntegerField(default=0, verbose_name='Question View Count')),
                ('submission_count', models.IntegerField(default=0, verbose_name='Submissions')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Question Poster')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Category', verbose_name='Category')),
            ],
            options={
                'ordering': ['-create_timestamp'],
            },
        ),
        migrations.CreateModel(
            name='QuestionView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_fail', models.PositiveIntegerField(default=0, editable=False, help_text='0 : Unknown Result, 1:Correct Answer,                                     2: Timeout, 3:Runtime Error, 4:Wrong Answer, 5:In progress', validators=[django.core.validators.MaxValueValidator(5)])),
                ('errors', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['submission', 'testcase'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('PY', 'Python2'), ('PY3', 'Python3')], max_length=5)),
                ('code', models.FileField(upload_to=questions.models.get_code_upload_url)),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0, 'The score can not be negative'), django.core.validators.MaxValueValidator(100.0, 'Total Score must be calculated as a percentage of 100')])),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('attempt_number', models.IntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['question', 'user', 'submitted_on'],
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Number : ')),
                ('input_file', models.FileField(help_text='Upload a .txt file that contains the input for this test case', upload_to=questions.models.get_testcase_input_upload_path, validators=[django.core.validators.FileExtensionValidator(['txt'], message='Only text files are allowed as input and outpur')], verbose_name='File Containing Input')),
                ('output_file', models.FileField(help_text='Upload a .txt file that contains the expected output for the above given input', upload_to=questions.models.get_testcase_output_upload_path, validators=[django.core.validators.FileExtensionValidator(['txt'], message='Only text files are allowed as input and output')], verbose_name='File Containing Expected Output')),
                ('points', models.PositiveIntegerField(default=10, help_text='The number of points that user will get if he/she completes this                                          test case successfully. The total points later-on will be calculated as a percentage of 100', verbose_name='Points')),
                ('last_edited_on', models.DateTimeField(auto_now=True, verbose_name='Last Edited On')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='Question')),
            ],
            options={
                'ordering': ['question', 'number'],
            },
        ),
        migrations.AddField(
            model_name='result',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Submission'),
        ),
        migrations.AddField(
            model_name='result',
            name='testcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.TestCase'),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together={('question', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='submission',
            unique_together={('question', 'user', 'attempt_number')},
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('testcase', 'submission')},
        ),
    ]
