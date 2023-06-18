# Makefile for Django project

# Variables
PYTHON = python
MANAGE = ./manage.py

# Default target
all: runserver

# Install dependencies
install:
	pip install -r requirements.txt

# Run development server
runserver:
	$(PYTHON) $(MANAGE) runserver

# Create database tables
migrate:
	$(PYTHON) $(MANAGE) migrate

#Migrate data in database
migrations:
	$(PYTHON) $(MANAGE) makemigrations $(CLASSNAME)

# make translation messages
messages:
	$(PYTHON) $(MANAGE) makemessages -l $(LANG)

# Create a new Django app
createapp:
	$(PYTHON) $(MANAGE) startapp $(APPNAME)

superuser:
	$(PYTHON) $(MANAGE) createsuperuser

# Run tests
test:
	$(PYTHON) $(MANAGE) test

collectstatic:
	$(PYTHON) $(MANAGE) collectstatic

# Clean up pycache and other temporary files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Show help
help:
	@echo "Available targets:"
	@echo "  install     : Install project dependencies"
	@echo "  runserver   : Run the development server"
	@echo "  migrate     : Apply database migrations"
	@echo "  createapp   : Create a new Django app"
	@echo "  test        : Run tests"
	@echo "  clean       : Clean up temporary files"
	@echo "  help        : Show this help message"

# Phony targets
.PHONY: all install runserver migrate createapp test clean help
