# Generated by Django 2.0.6 on 2020-04-20 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0002_auto_20200417_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student_id',
        ),
    ]
