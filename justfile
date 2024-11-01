i:
  uv sync && pre-commit install

export:
  uv export > requirements.txt

dev:
  uv run python main.py

build:
  scripts/build.sh

compile:
  uv run python tools/compile_qt.py

start: dev

run-hooks:
  pre-commit run --all-files

test: run-hooks
  ruff check

remove-hooks:
  pre-commit uninstall
