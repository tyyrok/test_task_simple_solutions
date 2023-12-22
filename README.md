# Тестовое задание для Простые Решения

## Установка
1. Копируем репозиторий
2. Создаем файл `.env.local` по примеру `.env.template`
3. Запускаем docker build `docker compose build`
4. Поднимаем docker контейнеры `docker compose up`
5. Загружаем fixtures из контейнера с Django `python manage.py loaddata api.json`

## Доступные endpoint
- `/buy/{item_id}/` - GET для получения json session.id
- `/item/{item_id}/` - GET страница с выводом информации о продукте с item_id

## ТЗ
### Описание задания:
1. 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
2.  Django Модель Item с полями (name, description, price)
3.  API с двумя методами:
    - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
4. Запуск используя Docker
5. Использование environment variables
6. Просмотр Django Моделей в Django Admin панели
