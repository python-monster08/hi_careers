# Generated by Django 5.0.3 on 2024-03-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_module', '0007_alter_question_correct_answer_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option_a',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('integer', 'Integer'), ('true_false', 'True/False')], max_length=20),
        ),
    ]
