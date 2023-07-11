.PHONY: all coverage install format github lint release test test-ci


PACKAGE := $(shell grep '^name =' pyproject.toml | cut -d '"' -f2)
DIR := $(subst -,_,$(PACKAGE))
VERSION := $(shell grep '^__version__ =' ${DIR}/__init__.py | cut -d '"' -f2)
LEAD := $(shell head -n 1 LEAD.md)


all:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

coverage:
	sensible-browser coverage/index.html

format:
	ruff $(DIR) tests --fix
	isort $(DIR) tests
	black $(DIR) tests

install:
	pip install --upgrade -e .[dev]

lint:
	ruff $(DIR) tests
	isort $(DIR) tests --check
	black $(DIR) tests --check
	# pyright $(DIR) tests

release:
	git checkout main && git pull origin && git fetch -p
	@git log --pretty=format:"%C(yellow)%h%Creset %s%Cgreen%d" --reverse -20
	@echo "\nReleasing v$(VERSION) in 10 seconds. Press <CTRL+C> to abort\n" && sleep 10
	make test && git commit -a -m 'v$(VERSION)' && git tag -a v$(VERSION) -m 'v$(VERSION)'
	git push --follow-tags

test:
	make lint
	pytest --cov ${DIR} --cov-report term-missing --cov-report html:coverage --cov-fail-under 70 --timeout=300

test-ci:
	make lint
	pytest --cov ${DIR} --cov-report term-missing --cov-report xml --cov-fail-under 80 --timeout=300 --ci
