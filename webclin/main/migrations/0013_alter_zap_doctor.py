# Generated by Django 4.2 on 2023-05-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_zap_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zap',
            name='doctor',
            field=models.CharField(max_length=20, null='Кузьмичева', verbose_name='Доктор'),
        ),
    ]
