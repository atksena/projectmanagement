# Generated by Django 4.1.7 on 2023-04-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_issue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='issue_type',
            field=models.BigIntegerField(null=True),
        ),
    ]
