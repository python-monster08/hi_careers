# Generated by Django 5.0.3 on 2024-03-07 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeOfDifficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='applicability',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='name_of_exam',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='negative_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='other',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_numbering_exam_paper',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='repeat_in_exam',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='sub_topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject_of_exam',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='year_of_exam',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='degree_of_difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_module.degreeofdifficulty'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_module.questiontype'),
        ),
    ]
