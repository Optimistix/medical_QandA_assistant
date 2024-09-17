FROM python:3.11-slim

WORKDIR /app

RUN pip install pipenv

COPY data/medquad.csv data/medquad.csv
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --ignore-pipfile --system

COPY medical_question_answering_assistant .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app
