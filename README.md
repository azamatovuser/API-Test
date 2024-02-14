# API-Test
**Как я выполнил?**
- Создайте на Django функционал регистрации и авторизации пользователей 
  - account/register/ = функционал регистрации
  - account/login/ = функционал авторизации
- После того как пользователь зарегистрировался и авторизовался он может заполнить информацию о себе и загрузить своё фото
  - account/detail/update/<account_id>/ = для заполнения информацию о себе и загрузить своё фото 
- К профилю пользователя можно добавлять текстовые комментарии
  - comment/list_or_create/ = пользователь может посмотреть все текстовые комментарии или добавить к профилю пользователя
  - метод POST требует авторизацию, а для GET не надо 
- Сделать API для пользователя
  - account/list/ - API для просмотра всех пользователей


Были использованы индексы, внешние ключи и для защиты секретных данных было использовано .env файл для хранения

**Как установить?**
- Сначала нужно клонировать проект и создать venv/env
- Установить необходимые вещи с помощью requirements.txt
- Создать новый файл с именем ".env" и заполнить как в "env_example"
- Сделать миграцию и создать superuser