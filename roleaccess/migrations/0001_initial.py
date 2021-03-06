# Generated by Django 2.1.5 on 2019-01-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'Permisisons',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default=None, max_length=60)),
                ('permission', models.ManyToManyField(to='roleaccess.Permissions')),
            ],
            options={
                'db_table': 'Roles',
            },
        ),
    ]
