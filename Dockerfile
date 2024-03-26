# For production deployment via Docker

FROM python:3.10-alpine

WORKDIR /code

ENV FLASK_SECRET_KEY='f(vih8_ex18l9nun93)&e+(yos+d$%f=!$5-4*lv5j#7br_!*n'
# ENV FLASK_APP=backend/app.py
# ENV FLASK_RUN_HOST=0.0.0.0

COPY backend/requirements.txt backend/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r backend/requirements.txt

COPY backend/. backend/.
COPY dist/. dist/.

EXPOSE 8000

CMD ["gunicorn",  "-b", "0.0.0.0:8000", "--chdir", "backend", "backend.wsgi", "--log-file", "-"]

