# CinemaApi

API
На каждый пункт нужен отдельный эндпоинт 
- список фильмов
- информация об одном конкретном фильме
- создание, удаление, изменение фильма (добавить сюда права доступа)
- список залов
*- информация про конкретный залл
*- создание, удаление, изменение зала (добавить сюда права доступа)
- афиша (список сеансов) по дате
*- афиша по фильму от даты до даты
*- афиша по залу от даты до даты
- информация о конкретном сеансе (фильм, зал, сколько мест занято)
- создание, изменение, удаление сеанса (добавить сюда права доступа)
- список мест в зале с флагами занято\свободно по номеру сеанса
- покупка билетов на сеанс


Реализация
- REST api обязательно
- права доступа сделать как угодно (сложно - Bearer и авторизация через соседний эндпоинт, просто - передать слово admin в хедере запроса, подойдёт что угодно)
*- покупка билетов должна предусматривать много запросов одновременно и не продавать одинаковые билеты разным людям
**- предусмотреть очистку билетов когда сеанс уже в прошлом (написать background job, должно загуглится что это такое)
*- юнит тесты
- все настройки хранить в отдельном json файле с конфигурацией (куда подключатся к базе, как часто запускать очиску билетов)
**- docker - завернуть всё в контейнеры, базу отдельно и прилагу отдельно, написать docker compose
**- написать миграции для базы данных и запускать процесс миграции перед стартом контейнера

Как предлагаю делать
Этап 1
  Придумать структуру базы данных - хранить можно какие угодно данные и как угодно, главное чтоб можно было реализовать все требования
  Сделать все задания без *
  В качестве базы данных можно использовать коллекции, если не знаешь как подключить какой-нибудь Postgres например

Этап 2
  Перейти на настоящую бд если сейчас она в памяти
  Сделать задания с одной *

Этап 3
  Задания с **
  Нужно научиться как работают контейнеры и что с ними можно делать, там достаточно много работы
