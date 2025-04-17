# Generated by Django 5.1.6 on 2025-04-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COMPANY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('aboutcompany', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT')], max_length=100)),
            ],
        ),
    ]
