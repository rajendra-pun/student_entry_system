# Generated by Django 3.2.13 on 2022-06-06 09:42

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
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=5)),
                ('address', models.CharField(max_length=100)),
                ('grade', models.IntegerField(default=1)),
                ('major', models.CharField(max_length=100)),
            ],
        ),
    ]
