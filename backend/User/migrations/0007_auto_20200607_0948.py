# Generated by Django 3.0.5 on 2020-06-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20200607_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_5',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_6',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_7',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_8',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
