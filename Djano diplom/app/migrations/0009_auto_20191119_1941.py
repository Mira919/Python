# Generated by Django 2.1.5 on 2019-11-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Автор'),
        ),
    ]