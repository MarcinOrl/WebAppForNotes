# Generated by Django 5.0.6 on 2024-06-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0007_goal_short_description_note_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
