## Запуск проекта
`docker-compose up -d`

## Запуск тестов

`docker-compose run web-service pytest`

## Генерация миграции

`docker-compose run web-service alembic revision --autogenerate`

## Запуск миграции

`docker-compose run web-service alembic upgrate head`