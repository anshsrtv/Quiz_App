# Generated by Django 3.1.2 on 2020-10-08 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20201008_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ans',
            new_name='ans_in_capitals',
        ),
    ]