# Generated by Django 4.2 on 2023-05-15 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_zap_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Картинки',
                'verbose_name_plural': 'Картиники',
            },
        ),
    ]
