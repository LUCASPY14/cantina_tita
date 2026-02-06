# Makefile
.PHONY: up down build logs shell-backend shell-frontend test migrate

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build --no-cache

logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

shell-backend:
	docker-compose exec backend bash

shell-frontend:
	docker-compose exec frontend bash

migrate:
	docker-compose exec backend python manage.py migrate

makemigrations:
	docker-compose exec backend python manage.py makemigrations

createsuperuser:
	docker-compose exec backend python manage.py createsuperuser

test:
	docker-compose exec backend python manage.py test

collectstatic:
	docker-compose exec backend python manage.py collectstatic --noinput
	docker-compose exec frontend python manage.py collectstatic --noinput

backup-db:
	docker-compose exec postgres pg_dump -U cantina_user cantina_tita > backup_$(date +%Y%m%d_%H%M%S).sql

restore-db:
	docker-compose exec -T postgres psql -U cantina_user cantina_tita < $(file)

# Desarrollo
dev:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml up

# Producción
prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d