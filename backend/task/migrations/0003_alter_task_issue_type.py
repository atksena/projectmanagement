# Generated by Django 4.1.7 on 2023-04-02 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='issue_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.issuetype'),
        ),
    ]
