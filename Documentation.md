# Документация по проекту
## Backend
## Приложение Main
### <a href="webclin/main/urls.py" target="_blank"> urls.py </a>
Содержит все url проекта:
  - Админ
  - Главная Казани
  - Главная Москвы
  - Запись Казани
  - Запись Москвы
  - Запись на приём
### <a href="webclin/main/views.py" target="_blank"> views.py </a>
Содержит представления для подлючения html страниц и записи в базу данных.  
Представления html:  
 - Подключение главной Казани
 - Подключение главной Москвы
 - Подключение запись Казани
 - Подключение запись Москвы
 - Создание записи на приём и добавление её в базу данных(3 представления)
### <a href="webclin/main/models.py" target="_blank"> models.py </a>
Содержит классы(модели), их описание и поля.  
Классы:  
 - Работники Казани
 - Работники Москвы
 - Запись на приём к конкретному доктору(3 класса)
 - Изображения
### <a href="webclin/main/admin.py" target="_blank"> admin.py </a>
Регистрация готовых баз данных для работы с ними от лица админа.
## Frontend
## HTML
### <a href="webclin/main/templates/main/kazan.html" target="_blank"> kazan.html </a>
Данный html файл содержит главную страницу нашего сайта для Казани.
### <a href="webclin/main/templates/main/msc.html" target="_blank"> msc.html </a>
Данный html файл содержит главную страницу нашего сайта для Московы.
### <a href="webclin/main/templates/main/zapiskaz.html" target="_blank"> zapiskaz.html </a>
Данный html файл содержит страницу для записи к ветеринару для Казани.
### <a href="webclin/main/templates/main/zapismsc.html" target="_blank"> zapismsc.html </a>
Данный html файл содержит страницу для записи к ветеринару для Москвы.
## CSS
### <a href="webclin/main/static/main/css/appointment.css" target="_blank"> appointment.css </a>
Данный css файл содержит стили для формы записи к ветеринару и для карточек врачей. Используется только на страницах для записик к ветеринару.
### <a href="webclin/main/static/main/css/main.css" target="_blank"> main.css </a>
Данный css файл содержит основные стили использующиеся для всех страниц, отвечает за шрифты, задний фон страниц и расстояние между элементами списка.
### <a href="webclin/main/static/main/css/contacts.css" target="_blank"> contacts.css </a>
Данный css файл содержит стили для нижней панели главных страниц, содержащую в себе контакты.

