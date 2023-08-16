# Generated by Django 4.2.4 on 2023-08-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('HardWare', 'HardWare')], max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
