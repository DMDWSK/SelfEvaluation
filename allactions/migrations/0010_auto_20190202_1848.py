# Generated by Django 2.1.5 on 2019-02-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allactions', '0009_auto_20190202_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='hint',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
