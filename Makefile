# Makefile default shell is /bin/sh
# we change to /bin/bash so that source will work.
SHELL := /bin/bash

runserver:
	cd backend && source ./env/bin/activate; flask --app app --debug run

runclient:
	cd frontend && npm run dev

build:
	cd frontend && npm run build