# Generated by Django 3.1 on 2020-11-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('esalary', models.IntegerField()),
                ('eaddress', models.CharField(max_length=50)),
            ],
        ),
    ]
