# Generated by Django 3.1 on 2020-10-11 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('p1_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('p2_id', models.AutoField(primary_key=True, serialize=False)),
                ('eno', models.IntegerField()),
                ('esalary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='mmiapp.parent2')),
                ('parent1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mmiapp.parent1')),
                ('no_of_projects', models.IntegerField()),
            ],
            bases=('mmiapp.parent1', 'mmiapp.parent2'),
        ),
    ]
