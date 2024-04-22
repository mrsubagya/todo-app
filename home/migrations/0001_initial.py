# Generated by Django 5.0.3 on 2024-03-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=1)),
            ],
        ),
    ]
