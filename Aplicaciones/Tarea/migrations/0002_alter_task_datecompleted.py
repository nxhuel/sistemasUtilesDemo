# Generated by Django 5.0.9 on 2024-11-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
