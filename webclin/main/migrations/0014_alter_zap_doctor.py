# Generated by Django 4.2 on 2023-05-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_zap_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zap',
            name='doctor',
            field=models.CharField(default='Кузьмичева', max_length=20, verbose_name='Доктор'),
        ),
    ]
