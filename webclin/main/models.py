from django.db import models

# Create your models here.

class Rabs(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    post = models.CharField('Должность', max_length=20)
    image = models.ImageField('Картинка', null=True, blank =True, upload_to='media')
    id1 = models.CharField('Id', max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'

class Rabs2(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    post = models.CharField('Должность', max_length=20)
    image = models.ImageField('Картинка', null=True, blank =True, upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работники2'
        verbose_name_plural = 'Работники2'

class Zap1(models.Model):
    name = models.CharField('Имя', max_length=20)
    phone = models.BigIntegerField('Телефон')
    doctor = models.CharField('Доктор', max_length=100, default='Кузьмичева Дарья Андреевна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ЗаписьКузьмичева'
        verbose_name_plural = 'ЗаписиКузьмичева'

class Zap2(models.Model):
    name = models.CharField('Имя', max_length=20)
    phone = models.BigIntegerField('Телефон')
    doctor = models.CharField('Доктор', max_length=100, default='Покровский Антон Иванов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ЗаписьПокровский'
        verbose_name_plural = 'ЗаписиПокровский'

class Zap3(models.Model):
    name = models.CharField('Имя', max_length=20)
    phone = models.BigIntegerField('Телефон')
    doctor = models.CharField('Доктор', max_length=100, default='Затина Альфия Габделхаевна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ЗаписьЗатина'
        verbose_name_plural = 'ЗаписиЗатина'

class Img(models.Model):
    image = models.ImageField('Картинка', null=True, blank =True, upload_to='media')


    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картиники'