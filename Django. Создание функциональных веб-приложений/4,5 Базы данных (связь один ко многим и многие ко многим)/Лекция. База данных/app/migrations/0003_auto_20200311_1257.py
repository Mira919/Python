# Generated by Django 2.2.5 on 2020-03-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200311_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, default=1, max_length=64),
            preserve_default=False,
        ),
    ]
