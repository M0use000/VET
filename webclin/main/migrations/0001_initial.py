# Generated by Django 4.2 on 2023-05-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=20)),
            ],
        ),
    ]
