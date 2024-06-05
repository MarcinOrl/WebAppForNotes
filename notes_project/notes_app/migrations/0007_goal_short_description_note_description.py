# Generated by Django 5.0.6 on 2024-06-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0006_tag_goal_tags_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]