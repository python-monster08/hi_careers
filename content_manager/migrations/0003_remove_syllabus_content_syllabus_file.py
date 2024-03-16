# Generated by Django 5.0.3 on 2024-03-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_manager', '0002_rename_exam_area_exam_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='content',
        ),
        migrations.AddField(
            model_name='syllabus',
            name='file',
            field=models.FileField(default=1, upload_to='SyllabusFiles'),
            preserve_default=False,
        ),
    ]