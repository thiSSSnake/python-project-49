install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

make brain-even:
	poetry run brain-even

make brain-calc:
	poetry run brain-calc	