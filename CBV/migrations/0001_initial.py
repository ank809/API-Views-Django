# Generated by Django 5.0.2 on 2024-02-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('reg_no', models.IntegerField()),
            ],
        ),
    ]
