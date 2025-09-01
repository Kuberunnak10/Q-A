# QnA API (FastAPI + PostgreSQL)

Сервис вопросов и ответов.

## Быстрый старт

1) Клонируйте репозиторий и перейдите в папку проекта:
```bash
git clone https://github.com/Kuberunnak10/Q-A.git
cd Q-A
```

2) Скопируйте пример окружения:
```bash
cp .env-example .env
```

3) Запустите контейнеры:
```bash
docker compose up -d --build
```

4) Откройте документацию (Swagger):
```
http://localhost:8000/docs
```

## Переменные окружения (.env)
Используются переменные для подключения к PostgreSQL:
```
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=fastapi_db
```

## Эндпоинты
Базовый префикс: `/api/v1`

Вопросы (Questions):
- GET `/questions/` — список всех вопросов
- POST `/questions/` — создать вопрос
- GET `/questions/{id}` — получить вопрос с ответами
- DELETE `/questions/{id}` — удалить вопрос (каскадно с ответами)

Ответы (Answers):
- POST `/questions/{id}/answers/` — добавить ответ к вопросу
- GET `/answers/{id}` — получить конкретный ответ
- DELETE `/answers/{id}` — удалить ответ

