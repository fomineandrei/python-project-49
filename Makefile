# Makefile
install: # Установка зависимостей и виртуального окружения
	poetry install

brain-games: # Запуск скрипта пакета brain-games
	poetry run brain-games

build: # Сборка пакета
	poetry build

publish: # Отладка публикации
	poetry publish --dry-run

package-install: # Установка пакета из файла whl
	python3 -m pip install --user dist/*.whl

lint: # Запуск линтера на проверку директории brain_games
	poetry run flake8 brain_games
