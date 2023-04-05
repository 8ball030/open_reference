FROM python:3.11 as base
RUN pip install poetry
COPY pyproject.toml poetry.lock .

RUN poetry install

CMD ["python", "manage.py", "runserver"]
